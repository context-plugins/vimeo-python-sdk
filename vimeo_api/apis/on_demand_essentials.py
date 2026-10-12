from __future__ import annotations

from uuid import UUID, uuid4

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
    async_empty_response,
    async_json_decoder,
    empty_response,
    json_body,
    json_decoder,
    param,
    raw_error_response,
    unwrap,
)
from ..errors.delete_vod_draft_error import DeleteVodDraftErrorBody, delete_vod_draft_error_mapper
from ..errors.edit_vod_error import EditVodErrorBody, edit_vod_error_mapper
from ..errors.get_user_vods_alt1_error import GetUserVodsAlt1ErrorBody, get_user_vods_alt1_error_mapper
from ..errors.get_user_vods_error import GetUserVodsErrorBody, get_user_vods_error_mapper
from ..errors.get_vod_error import GetVodErrorBody, get_vod_error_mapper
from ..models.enums.direction import DirectionOrStr
from ..models.enums.filter18 import Filter18OrStr
from ..models.enums.sort32 import Sort32OrStr
from ..models.me_ondemand_pages_request import MeOndemandPagesRequest, MeOndemandPagesRequestDict
from ..models.on_demand_page import OnDemandPage
from ..models.on_demand_page_connection import OnDemandPageConnection
from ..models.ondemand_pages_request import OndemandPagesRequest, OndemandPagesRequestDict
from ..models.users_ondemand_pages_request import UsersOndemandPagesRequest, UsersOndemandPagesRequestDict
from ..server.server import Server


class OnDemandEssentials:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = OnDemandEssentialsWithRawResponse(client, server, auth)

    def create_vod(
        self,
        user_id: float,
        body: UsersOndemandPagesRequest | UsersOndemandPagesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OnDemandPage:
        """This method creates a new On Demand page for the specified user. To publish the page, use the `edit
        <https://developer.vimeo.com/api/reference/on-demand#edit_vod>`__ method.

        Args:
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The On Demand page was created.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.create_vod(user_id, body, request_options=request_options))

    def create_vod_alt1(
        self,
        body: MeOndemandPagesRequest | MeOndemandPagesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OnDemandPage:
        """This method creates a new On Demand page for the specified user. To publish the page, use the `edit
        <https://developer.vimeo.com/api/reference/on-demand#edit_vod>`__ method.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The On Demand page was created.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.create_vod_alt1(body, request_options=request_options))

    def delete_vod_draft(self, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """This method deletes the specified On Demand page.

        Args:
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The On Demand page was deleted.

        Raises:
            ApiError: The authenticated user can't delete this On Demand page. No such On Demand page exists. ``error``
                is ``LegacyError | RawError``."""
        return unwrap(self._with_raw_response.delete_vod_draft(ondemand_id, request_options=request_options))

    def edit_vod(
        self,
        ondemand_id: float,
        *,
        body: OndemandPagesRequest | OndemandPagesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OnDemandPage:
        """This method edits the specified On Demand page. Use this method to enable preorders on the page or to publish
        the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The On Demand page was edited.

        Raises:
            ApiError: The authenticated user can't edit the On Demand page. No such On Demand page exists. ``error`` is
                ``LegacyError | RawError``."""
        return unwrap(self._with_raw_response.edit_vod(ondemand_id, body=body, request_options=request_options))

    def get_user_vods(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter18OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort32OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OnDemandPageConnection:
        """This method returns every On Demand page belonging to the authenticated user.

        Args:
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The type of the page to return. Option descriptions: * ``film`` - The page type is a film. *
                ``series`` - The page type is a series.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``added`` - Sort the results by most recently
                added page. * ``alphabetical`` - Sort the results alphabetically. * ``date`` - Sort the results by date.
                * ``modified_time`` - Sort the results by time of page modification. * ``name`` - Sort the results by
                page name. * ``publish.time`` - Sort the results by time of page publishing. * ``rating`` - Sort the
                results by content rating.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The On Demand pages were returned.

        Raises:
            ApiError: * No such user exists. * Error code 5451: This resource is restricted in your region. ``error`` is
                ``LegacyError | RawError``."""
        return unwrap(
            self._with_raw_response.get_user_vods(
                user_id,
                direction=direction,
                filter_=filter_,
                page=page,
                per_page=per_page,
                sort=sort,
                request_options=request_options,
            ),
        )

    def get_user_vods_alt1(
        self,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter18OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort32OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OnDemandPageConnection:
        """This method returns every On Demand page belonging to the authenticated user.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The type of the page to return. Option descriptions: * ``film`` - The page type is a film. *
                ``series`` - The page type is a series.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``added`` - Sort the results by most recently
                added page. * ``alphabetical`` - Sort the results alphabetically. * ``date`` - Sort the results by date.
                * ``modified_time`` - Sort the results by time of page modification. * ``name`` - Sort the results by
                page name. * ``publish.time`` - Sort the results by time of page publishing. * ``rating`` - Sort the
                results by content rating.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The On Demand pages were returned.

        Raises:
            ApiError: * No such user exists. * Error code 5451: This resource is restricted in your region. ``error`` is
                ``LegacyError | RawError``."""
        return unwrap(
            self._with_raw_response.get_user_vods_alt1(
                direction=direction,
                filter_=filter_,
                page=page,
                per_page=per_page,
                sort=sort,
                request_options=request_options,
            ),
        )

    def get_vod(self, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None) -> OnDemandPage:
        """This method returns the specified On Demand page.

        Args:
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The On Demand page was returned.

        Raises:
            ApiError: No such On Demand page exists. ``error`` is ``LegacyError | RawError``."""
        return unwrap(self._with_raw_response.get_vod(ondemand_id, request_options=request_options))

    @property
    def with_raw_response(self) -> OnDemandEssentialsWithRawResponse:
        return self._with_raw_response


class AsyncOnDemandEssentials:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncOnDemandEssentialsWithRawResponse(client, server, auth)

    async def create_vod(
        self,
        user_id: float,
        body: UsersOndemandPagesRequest | UsersOndemandPagesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OnDemandPage:
        """This method creates a new On Demand page for the specified user. To publish the page, use the `edit
        <https://developer.vimeo.com/api/reference/on-demand#edit_vod>`__ method.

        Args:
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The On Demand page was created.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.create_vod(user_id, body, request_options=request_options))

    async def create_vod_alt1(
        self,
        body: MeOndemandPagesRequest | MeOndemandPagesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OnDemandPage:
        """This method creates a new On Demand page for the specified user. To publish the page, use the `edit
        <https://developer.vimeo.com/api/reference/on-demand#edit_vod>`__ method.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The On Demand page was created.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.create_vod_alt1(body, request_options=request_options))

    async def delete_vod_draft(
        self, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes the specified On Demand page.

        Args:
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The On Demand page was deleted.

        Raises:
            ApiError: The authenticated user can't delete this On Demand page. No such On Demand page exists. ``error``
                is ``LegacyError | RawError``."""
        return unwrap(await self._with_raw_response.delete_vod_draft(ondemand_id, request_options=request_options))

    async def edit_vod(
        self,
        ondemand_id: float,
        *,
        body: OndemandPagesRequest | OndemandPagesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OnDemandPage:
        """This method edits the specified On Demand page. Use this method to enable preorders on the page or to publish
        the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The On Demand page was edited.

        Raises:
            ApiError: The authenticated user can't edit the On Demand page. No such On Demand page exists. ``error`` is
                ``LegacyError | RawError``."""
        return unwrap(await self._with_raw_response.edit_vod(ondemand_id, body=body, request_options=request_options))

    async def get_user_vods(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter18OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort32OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OnDemandPageConnection:
        """This method returns every On Demand page belonging to the authenticated user.

        Args:
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The type of the page to return. Option descriptions: * ``film`` - The page type is a film. *
                ``series`` - The page type is a series.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``added`` - Sort the results by most recently
                added page. * ``alphabetical`` - Sort the results alphabetically. * ``date`` - Sort the results by date.
                * ``modified_time`` - Sort the results by time of page modification. * ``name`` - Sort the results by
                page name. * ``publish.time`` - Sort the results by time of page publishing. * ``rating`` - Sort the
                results by content rating.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The On Demand pages were returned.

        Raises:
            ApiError: * No such user exists. * Error code 5451: This resource is restricted in your region. ``error`` is
                ``LegacyError | RawError``."""
        return unwrap(
            await self._with_raw_response.get_user_vods(
                user_id,
                direction=direction,
                filter_=filter_,
                page=page,
                per_page=per_page,
                sort=sort,
                request_options=request_options,
            ),
        )

    async def get_user_vods_alt1(
        self,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter18OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort32OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OnDemandPageConnection:
        """This method returns every On Demand page belonging to the authenticated user.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The type of the page to return. Option descriptions: * ``film`` - The page type is a film. *
                ``series`` - The page type is a series.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``added`` - Sort the results by most recently
                added page. * ``alphabetical`` - Sort the results alphabetically. * ``date`` - Sort the results by date.
                * ``modified_time`` - Sort the results by time of page modification. * ``name`` - Sort the results by
                page name. * ``publish.time`` - Sort the results by time of page publishing. * ``rating`` - Sort the
                results by content rating.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The On Demand pages were returned.

        Raises:
            ApiError: * No such user exists. * Error code 5451: This resource is restricted in your region. ``error`` is
                ``LegacyError | RawError``."""
        return unwrap(
            await self._with_raw_response.get_user_vods_alt1(
                direction=direction,
                filter_=filter_,
                page=page,
                per_page=per_page,
                sort=sort,
                request_options=request_options,
            ),
        )

    async def get_vod(self, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None) -> OnDemandPage:
        """This method returns the specified On Demand page.

        Args:
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The On Demand page was returned.

        Raises:
            ApiError: No such On Demand page exists. ``error`` is ``LegacyError | RawError``."""
        return unwrap(await self._with_raw_response.get_vod(ondemand_id, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncOnDemandEssentialsWithRawResponse:
        return self._with_raw_response


class OnDemandEssentialsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_vod(
        self,
        user_id: float,
        body: UsersOndemandPagesRequest | UsersOndemandPagesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OnDemandPage, RawError]:
        """This method creates a new On Demand page for the specified user. To publish the page, use the `edit
        <https://developer.vimeo.com/api/reference/on-demand#edit_vod>`__ method.

        Args:
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users/{user_id}/ondemand/pages"),
            path_params=[param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersOndemandPagesRequest | UsersOndemandPagesRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[OnDemandPage],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_vod_alt1(
        self,
        body: MeOndemandPagesRequest | MeOndemandPagesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OnDemandPage, RawError]:
        """This method creates a new On Demand page for the specified user. To publish the page, use the `edit
        <https://developer.vimeo.com/api/reference/on-demand#edit_vod>`__ method.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/me/ondemand/pages"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MeOndemandPagesRequest | MeOndemandPagesRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[OnDemandPage],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_vod_draft(
        self, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteVodDraftErrorBody]:
        """This method deletes the specified On Demand page.

        Args:
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}"),
            path_params=[param[float]("ondemand_id", ondemand_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_vod_draft_error_mapper,
            request_options=request_options,
        )

    def edit_vod(
        self,
        ondemand_id: float,
        *,
        body: OndemandPagesRequest | OndemandPagesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OnDemandPage, EditVodErrorBody]:
        """This method edits the specified On Demand page. Use this method to enable preorders on the page or to publish
        the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}"),
            path_params=[param[float]("ondemand_id", ondemand_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[OndemandPagesRequest | OndemandPagesRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[OnDemandPage],
            error_mapper=edit_vod_error_mapper,
            request_options=request_options,
        )

    def get_user_vods(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter18OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort32OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OnDemandPageConnection, GetUserVodsErrorBody]:
        """This method returns every On Demand page belonging to the authenticated user.

        Args:
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The type of the page to return. Option descriptions: * ``film`` - The page type is a film. *
                ``series`` - The page type is a series.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``added`` - Sort the results by most recently
                added page. * ``alphabetical`` - Sort the results alphabetically. * ``date`` - Sort the results by date.
                * ``modified_time`` - Sort the results by time of page modification. * ``name`` - Sort the results by
                page name. * ``publish.time`` - Sort the results by time of page publishing. * ``rating`` - Sort the
                results by content rating.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/ondemand/pages"),
            path_params=[param[float]("user_id", user_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[Filter18OrStr | None]("filter", filter_),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[Sort32OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[OnDemandPageConnection],
            error_mapper=get_user_vods_error_mapper,
            request_options=request_options,
        )

    def get_user_vods_alt1(
        self,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter18OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort32OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OnDemandPageConnection, GetUserVodsAlt1ErrorBody]:
        """This method returns every On Demand page belonging to the authenticated user.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The type of the page to return. Option descriptions: * ``film`` - The page type is a film. *
                ``series`` - The page type is a series.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``added`` - Sort the results by most recently
                added page. * ``alphabetical`` - Sort the results alphabetically. * ``date`` - Sort the results by date.
                * ``modified_time`` - Sort the results by time of page modification. * ``name`` - Sort the results by
                page name. * ``publish.time`` - Sort the results by time of page publishing. * ``rating`` - Sort the
                results by content rating.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/ondemand/pages"),
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[Filter18OrStr | None]("filter", filter_),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[Sort32OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[OnDemandPageConnection],
            error_mapper=get_user_vods_alt1_error_mapper,
            request_options=request_options,
        )

    def get_vod(
        self, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[OnDemandPage, GetVodErrorBody]:
        """This method returns the specified On Demand page.

        Args:
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}"),
            path_params=[param[float]("ondemand_id", ondemand_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[OnDemandPage],
            error_mapper=get_vod_error_mapper,
            request_options=request_options,
        )


class AsyncOnDemandEssentialsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_vod(
        self,
        user_id: float,
        body: UsersOndemandPagesRequest | UsersOndemandPagesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OnDemandPage, RawError]:
        """This method creates a new On Demand page for the specified user. To publish the page, use the `edit
        <https://developer.vimeo.com/api/reference/on-demand#edit_vod>`__ method.

        Args:
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users/{user_id}/ondemand/pages"),
            path_params=[param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersOndemandPagesRequest | UsersOndemandPagesRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[OnDemandPage],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_vod_alt1(
        self,
        body: MeOndemandPagesRequest | MeOndemandPagesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OnDemandPage, RawError]:
        """This method creates a new On Demand page for the specified user. To publish the page, use the `edit
        <https://developer.vimeo.com/api/reference/on-demand#edit_vod>`__ method.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/me/ondemand/pages"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MeOndemandPagesRequest | MeOndemandPagesRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[OnDemandPage],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_vod_draft(
        self, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteVodDraftErrorBody]:
        """This method deletes the specified On Demand page.

        Args:
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}"),
            path_params=[param[float]("ondemand_id", ondemand_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_empty_response,
            error_mapper=delete_vod_draft_error_mapper,
            request_options=request_options,
        )

    async def edit_vod(
        self,
        ondemand_id: float,
        *,
        body: OndemandPagesRequest | OndemandPagesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OnDemandPage, EditVodErrorBody]:
        """This method edits the specified On Demand page. Use this method to enable preorders on the page or to publish
        the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}"),
            path_params=[param[float]("ondemand_id", ondemand_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[OndemandPagesRequest | OndemandPagesRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[OnDemandPage],
            error_mapper=edit_vod_error_mapper,
            request_options=request_options,
        )

    async def get_user_vods(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter18OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort32OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OnDemandPageConnection, GetUserVodsErrorBody]:
        """This method returns every On Demand page belonging to the authenticated user.

        Args:
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The type of the page to return. Option descriptions: * ``film`` - The page type is a film. *
                ``series`` - The page type is a series.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``added`` - Sort the results by most recently
                added page. * ``alphabetical`` - Sort the results alphabetically. * ``date`` - Sort the results by date.
                * ``modified_time`` - Sort the results by time of page modification. * ``name`` - Sort the results by
                page name. * ``publish.time`` - Sort the results by time of page publishing. * ``rating`` - Sort the
                results by content rating.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/ondemand/pages"),
            path_params=[param[float]("user_id", user_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[Filter18OrStr | None]("filter", filter_),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[Sort32OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[OnDemandPageConnection],
            error_mapper=get_user_vods_error_mapper,
            request_options=request_options,
        )

    async def get_user_vods_alt1(
        self,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter18OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort32OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OnDemandPageConnection, GetUserVodsAlt1ErrorBody]:
        """This method returns every On Demand page belonging to the authenticated user.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The type of the page to return. Option descriptions: * ``film`` - The page type is a film. *
                ``series`` - The page type is a series.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``added`` - Sort the results by most recently
                added page. * ``alphabetical`` - Sort the results alphabetically. * ``date`` - Sort the results by date.
                * ``modified_time`` - Sort the results by time of page modification. * ``name`` - Sort the results by
                page name. * ``publish.time`` - Sort the results by time of page publishing. * ``rating`` - Sort the
                results by content rating.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/ondemand/pages"),
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[Filter18OrStr | None]("filter", filter_),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[Sort32OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[OnDemandPageConnection],
            error_mapper=get_user_vods_alt1_error_mapper,
            request_options=request_options,
        )

    async def get_vod(
        self, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[OnDemandPage, GetVodErrorBody]:
        """This method returns the specified On Demand page.

        Args:
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}"),
            path_params=[param[float]("ondemand_id", ondemand_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[OnDemandPage],
            error_mapper=get_vod_error_mapper,
            request_options=request_options,
        )
