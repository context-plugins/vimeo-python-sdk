from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AnySchemes,
    ApiResult,
    AsyncAnySchemes,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.enums.filter7 import Filter7OrStr
from ..models.language_connection import LanguageConnection
from ..server.server import Server


class VideosLanguages:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VideosLanguagesWithRawResponse(client, server, auth)

    def get_languages(
        self,
        *,
        filter: Filter7OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> LanguageConnection:
        """This method returns all available video languages.

        Args:
            filter: The attribute by which to filter the results. Option descriptions: * ``audiotracks`` - Return
                languages that can be used for audio tracks. * ``texttracks`` - Return languages that can be used for
                text tracks.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The languages were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_languages(
            filter=filter, page=page, per_page=per_page, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> VideosLanguagesWithRawResponse:
        return self._with_raw_response


class AsyncVideosLanguages:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVideosLanguagesWithRawResponse(client, server, auth)

    async def get_languages(
        self,
        *,
        filter: Filter7OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> LanguageConnection:
        """This method returns all available video languages.

        Args:
            filter: The attribute by which to filter the results. Option descriptions: * ``audiotracks`` - Return
                languages that can be used for audio tracks. * ``texttracks`` - Return languages that can be used for
                text tracks.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The languages were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_languages(
                filter=filter, page=page, per_page=per_page, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncVideosLanguagesWithRawResponse:
        return self._with_raw_response


class VideosLanguagesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_languages(
        self,
        *,
        filter: Filter7OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[LanguageConnection, RawError]:
        """This method returns all available video languages.

        Args:
            filter: The attribute by which to filter the results. Option descriptions: * ``audiotracks`` - Return
                languages that can be used for audio tracks. * ``texttracks`` - Return languages that can be used for
                text tracks.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/languages"),
            query_params=[
                param[Filter7OrStr | None]("filter", filter),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[LanguageConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncVideosLanguagesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_languages(
        self,
        *,
        filter: Filter7OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[LanguageConnection, RawError]:
        """This method returns all available video languages.

        Args:
            filter: The attribute by which to filter the results. Option descriptions: * ``audiotracks`` - Return
                languages that can be used for audio tracks. * ``texttracks`` - Return languages that can be used for
                text tracks.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/languages"),
            query_params=[
                param[Filter7OrStr | None]("filter", filter),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[LanguageConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
