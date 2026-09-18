import json
import re
import typing
import asyncio
from pathlib import Path

import httpx
import pytest

try:
    from envoapi import EnvoAPI, AsyncEnvoAPI, APIError, DecodeError, TransportError
except ImportError:
    EnvoAPI = AsyncEnvoAPI = APIError = DecodeError = TransportError = None

FIXTURES = Path(__file__).resolve().parents[2] / "tests" / "fixtures"
POSTS = json.loads((FIXTURES / "posts.json").read_text())
ERROR = json.loads((FIXTURES / "error.json").read_text())
OPERATIONS = json.loads((FIXTURES / "operations.json").read_text())
MANIFEST = json.loads((FIXTURES.parents[1] / "openapi" / "operations.json").read_text())


def normalized(value):
    if isinstance(value, dict):
        return {k: normalized(v) for k, v in value.items()}
    if isinstance(value, list):
        return [normalized(v) for v in value]
    if isinstance(value, str) and value.endswith("+00:00"):
        return value[:-6] + "Z"
    return value


@pytest.mark.parametrize("operation", MANIFEST, ids=lambda o: o["operationId"])
def test_operation_routing_and_model_roundtrip(operation):
    fixture = OPERATIONS[operation["operationId"]]
    calls = []

    def handle(request):
        calls.append(request)
        assert request.url.path == fixture["path"]
        assert dict(request.url.params) == {k: str(v) for k, v in fixture["query"].items()}
        return httpx.Response(200, json=fixture["response"])

    kwargs = {re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", k).lower(): v for k, v in fixture["query"].items()}
    # Generated parameter enums are part of the typed public model surface.
    if "reaction_type" in kwargs:
        from envoapi._generated.models.get_post_reactions_by_url_reaction_type import GetPostReactionsByUrlReactionType

        kwargs["reaction_type"] = GetPostReactionsByUrlReactionType(kwargs["reaction_type"])
    with EnvoAPI(api_key="key", transport=httpx.MockTransport(handle)) as client:
        result = getattr(getattr(client, operation["resource"]), operation["python"])(**kwargs)
        assert normalized(result.body.to_dict()) == fixture["response"]
    assert len(calls) == 1


def test_missing_credentials(monkeypatch):
    assert EnvoAPI is not None
    monkeypatch.delenv("ENVOAPI_API_KEY", raising=False)
    with pytest.raises(ValueError, match="API key"):
        EnvoAPI()


@pytest.mark.parametrize(
    "value,variant",
    [
        ({"publicId": "company_123", "name": None}, "CompanyReferenceType0"),
        ({"publicId": None, "name": "Sample company"}, "CompanyReferenceType1"),
        ({"publicId": "company_123", "name": "Sample company"}, "CompanyReferenceType2"),
    ],
)
def test_nullable_union_selects_the_correct_typed_branch(value, variant):
    from envoapi._generated.models.profile_company_interests_data import ProfileCompanyInterestsData

    parsed = ProfileCompanyInterestsData.from_dict({"companyInterests": [value]})
    assert type(parsed.company_interests[0]).__name__ == variant
    assert parsed.to_dict() == {"companyInterests": [value]}


def test_resource_annotations_resolve_for_all_operations():
    from envoapi import resources

    for operation in MANIFEST:
        for prefix in ("", "Async"):
            cls = getattr(resources, prefix + operation["resource"].capitalize())
            assert typing.get_type_hints(getattr(cls, operation["python"]))["return"]


@pytest.mark.asyncio
async def test_async_cancellation_propagates_without_retry():
    started = asyncio.Event()
    calls = []

    async def handle(request):
        calls.append(request)
        started.set()
        await asyncio.Event().wait()

    async with AsyncEnvoAPI(api_key="key", transport=httpx.MockTransport(handle)) as client:
        task = asyncio.create_task(client.profiles.get_posts(username="alice"))
        await asyncio.wait_for(started.wait(), 1)
        task.cancel()
        with pytest.raises(asyncio.CancelledError):
            await task
    assert len(calls) == 1


@pytest.mark.asyncio
async def test_async_error_preserves_metadata_without_retry():
    calls = []

    def handle(request):
        calls.append(request)
        return httpx.Response(429, json=ERROR, headers={"retry-after": "5"})

    async with AsyncEnvoAPI(api_key="key", transport=httpx.MockTransport(handle)) as client:
        with pytest.raises(APIError) as caught:
            await client.profiles.get_posts(username="alice")
        assert caught.value.request_id == "req_sdk_test"
        assert caught.value.headers["retry-after"] == "5"
    assert len(calls) == 1


def test_posts_preserve_envelope_and_send_one_request():
    assert EnvoAPI is not None
    calls = []

    def handle(request):
        calls.append(request)
        assert request.headers["authorization"] == "Bearer key"
        assert str(request.url) == "https://sdk.test/v1/profiles/posts?username=alice&cursor=cursor_Previous123"
        return httpx.Response(200, json=POSTS, headers={"x-request-id": "req_sdk_test"})

    with EnvoAPI(api_key="key", base_url="https://sdk.test", transport=httpx.MockTransport(handle)) as client:
        result = client.profiles.get_posts(username="alice", cursor="cursor_Previous123")
        assert result.body.to_dict() == POSTS
        assert result.body.meta.credit_cost == 1
        assert result.headers["x-request-id"] == "req_sdk_test"
        assert result.status == 200
    assert len(calls) == 1


@pytest.mark.parametrize(
    "status,code,retryable",
    [
        (400, "invalid_request", False),
        (401, "invalid_api_key", False),
        (404, "resource_not_found", False),
        (429, "rate_limit_exceeded", True),
        (503, "service_unavailable", True),
    ],
)
def test_api_errors_do_not_retry(status, code, retryable):
    assert EnvoAPI is not None
    calls = []

    def handle(request):
        calls.append(request)
        return httpx.Response(
            status,
            json={**ERROR, "error": {**ERROR["error"], "code": code, "retryable": retryable}},
            headers={"retry-after": "5"},
        )

    with EnvoAPI(api_key="key", transport=httpx.MockTransport(handle)) as client:
        with pytest.raises(APIError) as caught:
            client.profiles.get_posts(username="alice")
    error = caught.value
    assert (error.status, error.code, error.retryable, error.request_id) == (status, code, retryable, "req_sdk_test")
    assert error.headers["retry-after"] == "5"
    assert len(calls) == 1


def test_non_json_error():
    assert EnvoAPI is not None
    with EnvoAPI(
        api_key="key",
        transport=httpx.MockTransport(
            lambda r: httpx.Response(502, text="bad gateway", headers={"x-request-id": "req_proxy"})
        ),
    ) as client:
        with pytest.raises(APIError) as caught:
            client.profiles.get_posts(username="alice")
        assert (caught.value.status, caught.value.request_id) == (502, "req_proxy")


@pytest.mark.parametrize("body", ["{", "null", "{}"])
def test_decode_error(body):
    assert EnvoAPI is not None
    with EnvoAPI(api_key="key", transport=httpx.MockTransport(lambda r: httpx.Response(200, text=body))) as client:
        with pytest.raises(DecodeError):
            client.profiles.get_posts(username="alice")


def test_transport_error():
    assert EnvoAPI is not None

    def handle(request):
        raise httpx.ReadTimeout("timed out", request=request)

    with EnvoAPI(api_key="key", transport=httpx.MockTransport(handle)) as client:
        with pytest.raises(TransportError) as caught:
            client.profiles.get_posts(username="alice")
        assert isinstance(caught.value.__cause__, httpx.ReadTimeout)


@pytest.mark.asyncio
async def test_async_client():
    assert AsyncEnvoAPI is not None
    async with AsyncEnvoAPI(
        api_key="key", transport=httpx.MockTransport(lambda r: httpx.Response(200, json=POSTS))
    ) as client:
        result = await client.profiles.get_posts(username="alice")
        assert result.body.to_dict() == POSTS
