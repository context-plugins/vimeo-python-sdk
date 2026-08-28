from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AnySchemes,
    ApiResult,
    AsyncAnySchemes,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    empty_response,
    json_decoder,
    param,
)
from ..errors.add_video_privacy_domain_error import (
    AddVideoPrivacyDomainErrorBody,
    add_video_privacy_domain_error_mapper,
)
from ..errors.delete_video_privacy_domain_error import (
    DeleteVideoPrivacyDomainErrorBody,
    delete_video_privacy_domain_error_mapper,
)
from ..errors.get_video_privacy_domains_error import (
    GetVideoPrivacyDomainsErrorBody,
    get_video_privacy_domains_error_mapper,
)
from ..models.domain_connection import DomainConnection
from ..models.enums.direction import DirectionOrStr
from ..models.enums.sort78 import Sort78OrStr
from ..server.server import Server


class VideosEmbedPrivacy:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VideosEmbedPrivacyWithRawResponse(client, server, auth)

    def add_video_privacy_domain(
        self, domain: str, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method adds the specified domain to a video's allowlist.

        Args:
            domain: The domain name.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The domain was added to the video's allowlist.

        Raises:
            ApiError: The video doesn't have a user-defined access list. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.add_video_privacy_domain(
            domain, video_id, request_options=request_options
        ).unwrap()

    def delete_video_privacy_domain(
        self, domain: str, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method removes the specified domain from a video's allowlist.

        Args:
            domain: The domain name.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The domain was removed.

        Raises:
            ApiError: The video's embed privacy setting isn't ``whitelist``. No such domain exists. ``error`` is
                ``LegacyError | RawError``."""
        return self._with_raw_response.delete_video_privacy_domain(
            domain, video_id, request_options=request_options
        ).unwrap()

    def get_video_privacy_domains(
        self,
        video_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort78OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DomainConnection:
        """This method returns every domain on the specified video's allowlist.

        Args:
            video_id: The ID of the video.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``default`` - Sort the results by the video's
                allowlist ID.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The domains were returned.

        Raises:
            ApiError: There are no domains on which the video can be embedded. ``error`` is ``LegacyError |
                RawError``."""
        return self._with_raw_response.get_video_privacy_domains(
            video_id, direction=direction, page=page, per_page=per_page, sort=sort, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> VideosEmbedPrivacyWithRawResponse:
        return self._with_raw_response


class AsyncVideosEmbedPrivacy:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVideosEmbedPrivacyWithRawResponse(client, server, auth)

    async def add_video_privacy_domain(
        self, domain: str, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method adds the specified domain to a video's allowlist.

        Args:
            domain: The domain name.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The domain was added to the video's allowlist.

        Raises:
            ApiError: The video doesn't have a user-defined access list. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.add_video_privacy_domain(domain, video_id, request_options=request_options)
        ).unwrap()

    async def delete_video_privacy_domain(
        self, domain: str, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method removes the specified domain from a video's allowlist.

        Args:
            domain: The domain name.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The domain was removed.

        Raises:
            ApiError: The video's embed privacy setting isn't ``whitelist``. No such domain exists. ``error`` is
                ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.delete_video_privacy_domain(domain, video_id, request_options=request_options)
        ).unwrap()

    async def get_video_privacy_domains(
        self,
        video_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort78OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DomainConnection:
        """This method returns every domain on the specified video's allowlist.

        Args:
            video_id: The ID of the video.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``default`` - Sort the results by the video's
                allowlist ID.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The domains were returned.

        Raises:
            ApiError: There are no domains on which the video can be embedded. ``error`` is ``LegacyError |
                RawError``."""
        return (
            await self._with_raw_response.get_video_privacy_domains(
                video_id, direction=direction, page=page, per_page=per_page, sort=sort, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncVideosEmbedPrivacyWithRawResponse:
        return self._with_raw_response


class VideosEmbedPrivacyWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def add_video_privacy_domain(
        self, domain: str, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, AddVideoPrivacyDomainErrorBody]:
        """This method adds the specified domain to a video's allowlist.

        Args:
            domain: The domain name.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/videos/{video_id}/privacy/domains/{domain}"),
            path_params=[param[str]("domain", domain), param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=add_video_privacy_domain_error_mapper,
            request_options=request_options,
        )

    def delete_video_privacy_domain(
        self, domain: str, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteVideoPrivacyDomainErrorBody]:
        """This method removes the specified domain from a video's allowlist.

        Args:
            domain: The domain name.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/videos/{video_id}/privacy/domains/{domain}"),
            path_params=[param[str]("domain", domain), param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_video_privacy_domain_error_mapper,
            request_options=request_options,
        )

    def get_video_privacy_domains(
        self,
        video_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort78OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DomainConnection, GetVideoPrivacyDomainsErrorBody]:
        """This method returns every domain on the specified video's allowlist.

        Args:
            video_id: The ID of the video.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``default`` - Sort the results by the video's
                allowlist ID.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/privacy/domains"),
            path_params=[param[float]("video_id", video_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[Sort78OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[DomainConnection],
            error_mapper=get_video_privacy_domains_error_mapper,
            request_options=request_options,
        )


class AsyncVideosEmbedPrivacyWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def add_video_privacy_domain(
        self, domain: str, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, AddVideoPrivacyDomainErrorBody]:
        """This method adds the specified domain to a video's allowlist.

        Args:
            domain: The domain name.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/videos/{video_id}/privacy/domains/{domain}"),
            path_params=[param[str]("domain", domain), param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=add_video_privacy_domain_error_mapper,
            request_options=request_options,
        )

    async def delete_video_privacy_domain(
        self, domain: str, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteVideoPrivacyDomainErrorBody]:
        """This method removes the specified domain from a video's allowlist.

        Args:
            domain: The domain name.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/videos/{video_id}/privacy/domains/{domain}"),
            path_params=[param[str]("domain", domain), param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_video_privacy_domain_error_mapper,
            request_options=request_options,
        )

    async def get_video_privacy_domains(
        self,
        video_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort78OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DomainConnection, GetVideoPrivacyDomainsErrorBody]:
        """This method returns every domain on the specified video's allowlist.

        Args:
            video_id: The ID of the video.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``default`` - Sort the results by the video's
                allowlist ID.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/privacy/domains"),
            path_params=[param[float]("video_id", video_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[Sort78OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[DomainConnection],
            error_mapper=get_video_privacy_domains_error_mapper,
            request_options=request_options,
        )
