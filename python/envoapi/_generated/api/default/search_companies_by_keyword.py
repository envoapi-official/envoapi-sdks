from http import HTTPStatus
from typing import Any, Literal

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.company_domain_search_success import CompanyDomainSearchSuccess
from ...models.insufficient_credits_error_response import InsufficientCreditsErrorResponse
from ...models.internal_server_error_response import InternalServerErrorResponse
from ...models.invalid_api_key_error_response import InvalidApiKeyErrorResponse
from ...models.invalid_request_error_response import InvalidRequestErrorResponse
from ...models.lookup_forbidden_error_response import LookupForbiddenErrorResponse
from ...models.method_not_allowed_error_response import MethodNotAllowedErrorResponse
from ...models.not_acceptable_error_response import NotAcceptableErrorResponse
from ...models.rate_limit_exceeded_error_response import RateLimitExceededErrorResponse
from ...models.resource_not_found_error_response import ResourceNotFoundErrorResponse
from ...models.service_unavailable_error_response import ServiceUnavailableErrorResponse
from ...models.unsupported_media_type_error_response import UnsupportedMediaTypeErrorResponse
from ...models.upstream_error_response import UpstreamErrorResponse
from ...models.upstream_timeout_error_response import UpstreamTimeoutErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    keywords: str,
    offset: int | Unset = 0,
    location: str | Unset = UNSET,
    industry: str | Unset = UNSET,
    company_size: str | Unset = UNSET,
    has_jobs: Literal["true"] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["keywords"] = keywords

    params["offset"] = offset

    params["location"] = location

    params["industry"] = industry

    params["companySize"] = company_size

    params["hasJobs"] = has_jobs

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/companies/search",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CompanyDomainSearchSuccess
    | InsufficientCreditsErrorResponse
    | InternalServerErrorResponse
    | InvalidApiKeyErrorResponse
    | InvalidRequestErrorResponse
    | LookupForbiddenErrorResponse
    | MethodNotAllowedErrorResponse
    | NotAcceptableErrorResponse
    | RateLimitExceededErrorResponse
    | ResourceNotFoundErrorResponse
    | ServiceUnavailableErrorResponse
    | UnsupportedMediaTypeErrorResponse
    | UpstreamErrorResponse
    | UpstreamTimeoutErrorResponse
    | None
):
    if response.status_code == 200:
        response_200 = CompanyDomainSearchSuccess.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = InvalidRequestErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = InvalidApiKeyErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = InsufficientCreditsErrorResponse.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = LookupForbiddenErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ResourceNotFoundErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = MethodNotAllowedErrorResponse.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = NotAcceptableErrorResponse.from_dict(response.json())

        return response_406

    if response.status_code == 415:
        response_415 = UnsupportedMediaTypeErrorResponse.from_dict(response.json())

        return response_415

    if response.status_code == 429:
        response_429 = RateLimitExceededErrorResponse.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = InternalServerErrorResponse.from_dict(response.json())

        return response_500

    if response.status_code == 502:
        response_502 = UpstreamErrorResponse.from_dict(response.json())

        return response_502

    if response.status_code == 503:
        response_503 = ServiceUnavailableErrorResponse.from_dict(response.json())

        return response_503

    if response.status_code == 504:
        response_504 = UpstreamTimeoutErrorResponse.from_dict(response.json())

        return response_504

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CompanyDomainSearchSuccess
    | InsufficientCreditsErrorResponse
    | InternalServerErrorResponse
    | InvalidApiKeyErrorResponse
    | InvalidRequestErrorResponse
    | LookupForbiddenErrorResponse
    | MethodNotAllowedErrorResponse
    | NotAcceptableErrorResponse
    | RateLimitExceededErrorResponse
    | ResourceNotFoundErrorResponse
    | ServiceUnavailableErrorResponse
    | UnsupportedMediaTypeErrorResponse
    | UpstreamErrorResponse
    | UpstreamTimeoutErrorResponse
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    keywords: str,
    offset: int | Unset = 0,
    location: str | Unset = UNSET,
    industry: str | Unset = UNSET,
    company_size: str | Unset = UNSET,
    has_jobs: Literal["true"] | Unset = UNSET,
) -> Response[
    CompanyDomainSearchSuccess
    | InsufficientCreditsErrorResponse
    | InternalServerErrorResponse
    | InvalidApiKeyErrorResponse
    | InvalidRequestErrorResponse
    | LookupForbiddenErrorResponse
    | MethodNotAllowedErrorResponse
    | NotAcceptableErrorResponse
    | RateLimitExceededErrorResponse
    | ResourceNotFoundErrorResponse
    | ServiceUnavailableErrorResponse
    | UnsupportedMediaTypeErrorResponse
    | UpstreamErrorResponse
    | UpstreamTimeoutErrorResponse
]:
    """Search LinkedIn companies by keyword.

    Args:
        keywords (str):
        offset (int | Unset):  Default: 0.
        location (str | Unset): Up to 10 IDs from [Location search](../searchlocationsbykeyword/)
            (`data.locations[].id`), separated by commas. Matches any listed location, including
            branch offices. All other filters must also match.
        industry (str | Unset): Up to 10 IDs from [Industry search](../searchindustriesbykeyword/)
            (`data.industries[].id`), separated by commas. Matches any listed industry. All other
            filters must also match.
        company_size (str | Unset): Comma-separated employee-count buckets: B=1–10, C=11–50,
            D=51–200, E=201–500, F=501–1,000, G=1,001–5,000, H=5,001–10,000, I=10,001+. Use unique
            values; multiple buckets are OR.
        has_jobs (Literal['true'] | Unset): Set true to require job listings on LinkedIn. Omit for
            unrestricted results. false and 1 are not accepted; filtering for companies without jobs
            is not supported.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompanyDomainSearchSuccess | InsufficientCreditsErrorResponse | InternalServerErrorResponse | InvalidApiKeyErrorResponse | InvalidRequestErrorResponse | LookupForbiddenErrorResponse | MethodNotAllowedErrorResponse | NotAcceptableErrorResponse | RateLimitExceededErrorResponse | ResourceNotFoundErrorResponse | ServiceUnavailableErrorResponse | UnsupportedMediaTypeErrorResponse | UpstreamErrorResponse | UpstreamTimeoutErrorResponse]
    """

    kwargs = _get_kwargs(
        keywords=keywords,
        offset=offset,
        location=location,
        industry=industry,
        company_size=company_size,
        has_jobs=has_jobs,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    keywords: str,
    offset: int | Unset = 0,
    location: str | Unset = UNSET,
    industry: str | Unset = UNSET,
    company_size: str | Unset = UNSET,
    has_jobs: Literal["true"] | Unset = UNSET,
) -> (
    CompanyDomainSearchSuccess
    | InsufficientCreditsErrorResponse
    | InternalServerErrorResponse
    | InvalidApiKeyErrorResponse
    | InvalidRequestErrorResponse
    | LookupForbiddenErrorResponse
    | MethodNotAllowedErrorResponse
    | NotAcceptableErrorResponse
    | RateLimitExceededErrorResponse
    | ResourceNotFoundErrorResponse
    | ServiceUnavailableErrorResponse
    | UnsupportedMediaTypeErrorResponse
    | UpstreamErrorResponse
    | UpstreamTimeoutErrorResponse
    | None
):
    """Search LinkedIn companies by keyword.

    Args:
        keywords (str):
        offset (int | Unset):  Default: 0.
        location (str | Unset): Up to 10 IDs from [Location search](../searchlocationsbykeyword/)
            (`data.locations[].id`), separated by commas. Matches any listed location, including
            branch offices. All other filters must also match.
        industry (str | Unset): Up to 10 IDs from [Industry search](../searchindustriesbykeyword/)
            (`data.industries[].id`), separated by commas. Matches any listed industry. All other
            filters must also match.
        company_size (str | Unset): Comma-separated employee-count buckets: B=1–10, C=11–50,
            D=51–200, E=201–500, F=501–1,000, G=1,001–5,000, H=5,001–10,000, I=10,001+. Use unique
            values; multiple buckets are OR.
        has_jobs (Literal['true'] | Unset): Set true to require job listings on LinkedIn. Omit for
            unrestricted results. false and 1 are not accepted; filtering for companies without jobs
            is not supported.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompanyDomainSearchSuccess | InsufficientCreditsErrorResponse | InternalServerErrorResponse | InvalidApiKeyErrorResponse | InvalidRequestErrorResponse | LookupForbiddenErrorResponse | MethodNotAllowedErrorResponse | NotAcceptableErrorResponse | RateLimitExceededErrorResponse | ResourceNotFoundErrorResponse | ServiceUnavailableErrorResponse | UnsupportedMediaTypeErrorResponse | UpstreamErrorResponse | UpstreamTimeoutErrorResponse
    """

    return sync_detailed(
        client=client,
        keywords=keywords,
        offset=offset,
        location=location,
        industry=industry,
        company_size=company_size,
        has_jobs=has_jobs,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    keywords: str,
    offset: int | Unset = 0,
    location: str | Unset = UNSET,
    industry: str | Unset = UNSET,
    company_size: str | Unset = UNSET,
    has_jobs: Literal["true"] | Unset = UNSET,
) -> Response[
    CompanyDomainSearchSuccess
    | InsufficientCreditsErrorResponse
    | InternalServerErrorResponse
    | InvalidApiKeyErrorResponse
    | InvalidRequestErrorResponse
    | LookupForbiddenErrorResponse
    | MethodNotAllowedErrorResponse
    | NotAcceptableErrorResponse
    | RateLimitExceededErrorResponse
    | ResourceNotFoundErrorResponse
    | ServiceUnavailableErrorResponse
    | UnsupportedMediaTypeErrorResponse
    | UpstreamErrorResponse
    | UpstreamTimeoutErrorResponse
]:
    """Search LinkedIn companies by keyword.

    Args:
        keywords (str):
        offset (int | Unset):  Default: 0.
        location (str | Unset): Up to 10 IDs from [Location search](../searchlocationsbykeyword/)
            (`data.locations[].id`), separated by commas. Matches any listed location, including
            branch offices. All other filters must also match.
        industry (str | Unset): Up to 10 IDs from [Industry search](../searchindustriesbykeyword/)
            (`data.industries[].id`), separated by commas. Matches any listed industry. All other
            filters must also match.
        company_size (str | Unset): Comma-separated employee-count buckets: B=1–10, C=11–50,
            D=51–200, E=201–500, F=501–1,000, G=1,001–5,000, H=5,001–10,000, I=10,001+. Use unique
            values; multiple buckets are OR.
        has_jobs (Literal['true'] | Unset): Set true to require job listings on LinkedIn. Omit for
            unrestricted results. false and 1 are not accepted; filtering for companies without jobs
            is not supported.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompanyDomainSearchSuccess | InsufficientCreditsErrorResponse | InternalServerErrorResponse | InvalidApiKeyErrorResponse | InvalidRequestErrorResponse | LookupForbiddenErrorResponse | MethodNotAllowedErrorResponse | NotAcceptableErrorResponse | RateLimitExceededErrorResponse | ResourceNotFoundErrorResponse | ServiceUnavailableErrorResponse | UnsupportedMediaTypeErrorResponse | UpstreamErrorResponse | UpstreamTimeoutErrorResponse]
    """

    kwargs = _get_kwargs(
        keywords=keywords,
        offset=offset,
        location=location,
        industry=industry,
        company_size=company_size,
        has_jobs=has_jobs,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    keywords: str,
    offset: int | Unset = 0,
    location: str | Unset = UNSET,
    industry: str | Unset = UNSET,
    company_size: str | Unset = UNSET,
    has_jobs: Literal["true"] | Unset = UNSET,
) -> (
    CompanyDomainSearchSuccess
    | InsufficientCreditsErrorResponse
    | InternalServerErrorResponse
    | InvalidApiKeyErrorResponse
    | InvalidRequestErrorResponse
    | LookupForbiddenErrorResponse
    | MethodNotAllowedErrorResponse
    | NotAcceptableErrorResponse
    | RateLimitExceededErrorResponse
    | ResourceNotFoundErrorResponse
    | ServiceUnavailableErrorResponse
    | UnsupportedMediaTypeErrorResponse
    | UpstreamErrorResponse
    | UpstreamTimeoutErrorResponse
    | None
):
    """Search LinkedIn companies by keyword.

    Args:
        keywords (str):
        offset (int | Unset):  Default: 0.
        location (str | Unset): Up to 10 IDs from [Location search](../searchlocationsbykeyword/)
            (`data.locations[].id`), separated by commas. Matches any listed location, including
            branch offices. All other filters must also match.
        industry (str | Unset): Up to 10 IDs from [Industry search](../searchindustriesbykeyword/)
            (`data.industries[].id`), separated by commas. Matches any listed industry. All other
            filters must also match.
        company_size (str | Unset): Comma-separated employee-count buckets: B=1–10, C=11–50,
            D=51–200, E=201–500, F=501–1,000, G=1,001–5,000, H=5,001–10,000, I=10,001+. Use unique
            values; multiple buckets are OR.
        has_jobs (Literal['true'] | Unset): Set true to require job listings on LinkedIn. Omit for
            unrestricted results. false and 1 are not accepted; filtering for companies without jobs
            is not supported.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompanyDomainSearchSuccess | InsufficientCreditsErrorResponse | InternalServerErrorResponse | InvalidApiKeyErrorResponse | InvalidRequestErrorResponse | LookupForbiddenErrorResponse | MethodNotAllowedErrorResponse | NotAcceptableErrorResponse | RateLimitExceededErrorResponse | ResourceNotFoundErrorResponse | ServiceUnavailableErrorResponse | UnsupportedMediaTypeErrorResponse | UpstreamErrorResponse | UpstreamTimeoutErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            keywords=keywords,
            offset=offset,
            location=location,
            industry=industry,
            company_size=company_size,
            has_jobs=has_jobs,
        )
    ).parsed
