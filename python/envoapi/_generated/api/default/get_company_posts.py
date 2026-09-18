from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.company_posts_success import CompanyPostsSuccess
from ...models.get_company_posts_filter import GetCompanyPostsFilter
from ...models.insufficient_credits_error_response import InsufficientCreditsErrorResponse
from ...models.internal_server_error_response import InternalServerErrorResponse
from ...models.invalid_api_key_error_response import InvalidApiKeyErrorResponse
from ...models.lookup_forbidden_error_response import LookupForbiddenErrorResponse
from ...models.method_not_allowed_error_response import MethodNotAllowedErrorResponse
from ...models.not_acceptable_error_response import NotAcceptableErrorResponse
from ...models.profile_posts_invalid_request_response import ProfilePostsInvalidRequestResponse
from ...models.rate_limit_exceeded_error_response import RateLimitExceededErrorResponse
from ...models.resource_not_found_error_response import ResourceNotFoundErrorResponse
from ...models.service_unavailable_error_response import ServiceUnavailableErrorResponse
from ...models.unsupported_media_type_error_response import UnsupportedMediaTypeErrorResponse
from ...models.upstream_error_response import UpstreamErrorResponse
from ...models.upstream_timeout_error_response import UpstreamTimeoutErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    slug: str,
    filter_: GetCompanyPostsFilter | Unset = GetCompanyPostsFilter.ALL,
    start: int | Unset = 0,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["slug"] = slug

    json_filter_: str | Unset = UNSET
    if not isinstance(filter_, Unset):
        json_filter_ = filter_.value

    params["filter"] = json_filter_

    params["start"] = start

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/companies/posts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CompanyPostsSuccess
    | InsufficientCreditsErrorResponse
    | InternalServerErrorResponse
    | InvalidApiKeyErrorResponse
    | LookupForbiddenErrorResponse
    | MethodNotAllowedErrorResponse
    | NotAcceptableErrorResponse
    | ProfilePostsInvalidRequestResponse
    | RateLimitExceededErrorResponse
    | ResourceNotFoundErrorResponse
    | ServiceUnavailableErrorResponse
    | UnsupportedMediaTypeErrorResponse
    | UpstreamErrorResponse
    | UpstreamTimeoutErrorResponse
    | None
):
    if response.status_code == 200:
        response_200 = CompanyPostsSuccess.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ProfilePostsInvalidRequestResponse.from_dict(response.json())

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
    CompanyPostsSuccess
    | InsufficientCreditsErrorResponse
    | InternalServerErrorResponse
    | InvalidApiKeyErrorResponse
    | LookupForbiddenErrorResponse
    | MethodNotAllowedErrorResponse
    | NotAcceptableErrorResponse
    | ProfilePostsInvalidRequestResponse
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
    slug: str,
    filter_: GetCompanyPostsFilter | Unset = GetCompanyPostsFilter.ALL,
    start: int | Unset = 0,
    cursor: str | Unset = UNSET,
) -> Response[
    CompanyPostsSuccess
    | InsufficientCreditsErrorResponse
    | InternalServerErrorResponse
    | InvalidApiKeyErrorResponse
    | LookupForbiddenErrorResponse
    | MethodNotAllowedErrorResponse
    | NotAcceptableErrorResponse
    | ProfilePostsInvalidRequestResponse
    | RateLimitExceededErrorResponse
    | ResourceNotFoundErrorResponse
    | ServiceUnavailableErrorResponse
    | UnsupportedMediaTypeErrorResponse
    | UpstreamErrorResponse
    | UpstreamTimeoutErrorResponse
]:
    """Get Company posts.

    Args:
        slug (str):
        filter_ (GetCompanyPostsFilter | Unset):  Default: GetCompanyPostsFilter.ALL.
        start (int | Unset): Initial offset. With a cursor, omit start or supply its next offset;
            the cursor determines continuation. Default: 0.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompanyPostsSuccess | InsufficientCreditsErrorResponse | InternalServerErrorResponse | InvalidApiKeyErrorResponse | LookupForbiddenErrorResponse | MethodNotAllowedErrorResponse | NotAcceptableErrorResponse | ProfilePostsInvalidRequestResponse | RateLimitExceededErrorResponse | ResourceNotFoundErrorResponse | ServiceUnavailableErrorResponse | UnsupportedMediaTypeErrorResponse | UpstreamErrorResponse | UpstreamTimeoutErrorResponse]
    """

    kwargs = _get_kwargs(
        slug=slug,
        filter_=filter_,
        start=start,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    slug: str,
    filter_: GetCompanyPostsFilter | Unset = GetCompanyPostsFilter.ALL,
    start: int | Unset = 0,
    cursor: str | Unset = UNSET,
) -> (
    CompanyPostsSuccess
    | InsufficientCreditsErrorResponse
    | InternalServerErrorResponse
    | InvalidApiKeyErrorResponse
    | LookupForbiddenErrorResponse
    | MethodNotAllowedErrorResponse
    | NotAcceptableErrorResponse
    | ProfilePostsInvalidRequestResponse
    | RateLimitExceededErrorResponse
    | ResourceNotFoundErrorResponse
    | ServiceUnavailableErrorResponse
    | UnsupportedMediaTypeErrorResponse
    | UpstreamErrorResponse
    | UpstreamTimeoutErrorResponse
    | None
):
    """Get Company posts.

    Args:
        slug (str):
        filter_ (GetCompanyPostsFilter | Unset):  Default: GetCompanyPostsFilter.ALL.
        start (int | Unset): Initial offset. With a cursor, omit start or supply its next offset;
            the cursor determines continuation. Default: 0.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompanyPostsSuccess | InsufficientCreditsErrorResponse | InternalServerErrorResponse | InvalidApiKeyErrorResponse | LookupForbiddenErrorResponse | MethodNotAllowedErrorResponse | NotAcceptableErrorResponse | ProfilePostsInvalidRequestResponse | RateLimitExceededErrorResponse | ResourceNotFoundErrorResponse | ServiceUnavailableErrorResponse | UnsupportedMediaTypeErrorResponse | UpstreamErrorResponse | UpstreamTimeoutErrorResponse
    """

    return sync_detailed(
        client=client,
        slug=slug,
        filter_=filter_,
        start=start,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    slug: str,
    filter_: GetCompanyPostsFilter | Unset = GetCompanyPostsFilter.ALL,
    start: int | Unset = 0,
    cursor: str | Unset = UNSET,
) -> Response[
    CompanyPostsSuccess
    | InsufficientCreditsErrorResponse
    | InternalServerErrorResponse
    | InvalidApiKeyErrorResponse
    | LookupForbiddenErrorResponse
    | MethodNotAllowedErrorResponse
    | NotAcceptableErrorResponse
    | ProfilePostsInvalidRequestResponse
    | RateLimitExceededErrorResponse
    | ResourceNotFoundErrorResponse
    | ServiceUnavailableErrorResponse
    | UnsupportedMediaTypeErrorResponse
    | UpstreamErrorResponse
    | UpstreamTimeoutErrorResponse
]:
    """Get Company posts.

    Args:
        slug (str):
        filter_ (GetCompanyPostsFilter | Unset):  Default: GetCompanyPostsFilter.ALL.
        start (int | Unset): Initial offset. With a cursor, omit start or supply its next offset;
            the cursor determines continuation. Default: 0.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompanyPostsSuccess | InsufficientCreditsErrorResponse | InternalServerErrorResponse | InvalidApiKeyErrorResponse | LookupForbiddenErrorResponse | MethodNotAllowedErrorResponse | NotAcceptableErrorResponse | ProfilePostsInvalidRequestResponse | RateLimitExceededErrorResponse | ResourceNotFoundErrorResponse | ServiceUnavailableErrorResponse | UnsupportedMediaTypeErrorResponse | UpstreamErrorResponse | UpstreamTimeoutErrorResponse]
    """

    kwargs = _get_kwargs(
        slug=slug,
        filter_=filter_,
        start=start,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    slug: str,
    filter_: GetCompanyPostsFilter | Unset = GetCompanyPostsFilter.ALL,
    start: int | Unset = 0,
    cursor: str | Unset = UNSET,
) -> (
    CompanyPostsSuccess
    | InsufficientCreditsErrorResponse
    | InternalServerErrorResponse
    | InvalidApiKeyErrorResponse
    | LookupForbiddenErrorResponse
    | MethodNotAllowedErrorResponse
    | NotAcceptableErrorResponse
    | ProfilePostsInvalidRequestResponse
    | RateLimitExceededErrorResponse
    | ResourceNotFoundErrorResponse
    | ServiceUnavailableErrorResponse
    | UnsupportedMediaTypeErrorResponse
    | UpstreamErrorResponse
    | UpstreamTimeoutErrorResponse
    | None
):
    """Get Company posts.

    Args:
        slug (str):
        filter_ (GetCompanyPostsFilter | Unset):  Default: GetCompanyPostsFilter.ALL.
        start (int | Unset): Initial offset. With a cursor, omit start or supply its next offset;
            the cursor determines continuation. Default: 0.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompanyPostsSuccess | InsufficientCreditsErrorResponse | InternalServerErrorResponse | InvalidApiKeyErrorResponse | LookupForbiddenErrorResponse | MethodNotAllowedErrorResponse | NotAcceptableErrorResponse | ProfilePostsInvalidRequestResponse | RateLimitExceededErrorResponse | ResourceNotFoundErrorResponse | ServiceUnavailableErrorResponse | UnsupportedMediaTypeErrorResponse | UpstreamErrorResponse | UpstreamTimeoutErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            slug=slug,
            filter_=filter_,
            start=start,
            cursor=cursor,
        )
    ).parsed
