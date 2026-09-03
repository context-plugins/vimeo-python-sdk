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
    empty_response,
    json_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..errors.add_folder_to_showcases_error import AddFolderToShowcasesErrorBody, add_folder_to_showcases_error_mapper
from ..errors.copy_showcase_alt2_error import CopyShowcaseAlt2ErrorBody, copy_showcase_alt2_error_mapper
from ..errors.copy_showcase_error import CopyShowcaseErrorBody, copy_showcase_error_mapper
from ..errors.create_showcase_alt1_error import CreateShowcaseAlt1ErrorBody, create_showcase_alt1_error_mapper
from ..errors.create_showcase_error import CreateShowcaseErrorBody, create_showcase_error_mapper
from ..errors.delete_showcase_alt2_error import DeleteShowcaseAlt2ErrorBody, delete_showcase_alt2_error_mapper
from ..errors.delete_showcase_error import DeleteShowcaseErrorBody, delete_showcase_error_mapper
from ..errors.edit_showcase_alt2_error import EditShowcaseAlt2ErrorBody, edit_showcase_alt2_error_mapper
from ..errors.edit_showcase_error import EditShowcaseErrorBody, edit_showcase_error_mapper
from ..errors.get_showcase_alt2_error import GetShowcaseAlt2ErrorBody, get_showcase_alt2_error_mapper
from ..errors.get_showcase_error import GetShowcaseErrorBody, get_showcase_error_mapper
from ..errors.get_showcases_alt1_error import GetShowcasesAlt1ErrorBody, get_showcases_alt1_error_mapper
from ..errors.get_showcases_error import GetShowcasesErrorBody, get_showcases_error_mapper
from ..models.album import Album
from ..models.album_connection import AlbumConnection
from ..models.enums.direction import DirectionOrStr
from ..models.enums.sort18 import Sort18OrStr
from ..models.me_albums_copy_request import MeAlbumsCopyRequest, MeAlbumsCopyRequestDict
from ..models.me_albums_request import MeAlbumsRequest, MeAlbumsRequestDict
from ..models.me_albums_request1 import MeAlbumsRequest1, MeAlbumsRequest1Dict
from ..models.users_albums_copy_request import UsersAlbumsCopyRequest, UsersAlbumsCopyRequestDict
from ..models.users_albums_request import UsersAlbumsRequest, UsersAlbumsRequestDict
from ..models.users_albums_request1 import UsersAlbumsRequest1, UsersAlbumsRequest1Dict
from ..server.server import Server


class ShowcasesEssentials:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ShowcasesEssentialsWithRawResponse(client, server, auth)

    def add_folder_to_showcases(
        self, user_id: float, album_uris: str, folder_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method adds all videos and events from a specified folder to showcases.

        The authenticated user must either be the owner of the showcase or have team permissions.

        Args:
            user_id: The ID of the user.
            album_uris: A comma-separated list of showcase URIs.
            folder_id: The ID of the folder containing videos and events to add.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The folder contents were added to the showcases.

        Raises:
            ApiError: Error code 2204: A parameter is invalid. Error code 3200: The user lacks the permissions to update
                the showcases or access the folder. Error code 5000: The folder was not found. ``error`` is ``Error |
                RawError``."""
        return self._with_raw_response.add_folder_to_showcases(
            user_id, album_uris, folder_id, request_options=request_options
        ).unwrap()

    def copy_showcase(
        self,
        album_id: float,
        user_id: float,
        *,
        body: UsersAlbumsCopyRequest | UsersAlbumsCopyRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Album:
        """This method creates a copy of the specified showcase.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The copied showcase was created.

        Raises:
            ApiError: The authenticated user can't copy this showcase. No such showcase exists. ``error`` is
                ``LegacyError | RawError``."""
        return self._with_raw_response.copy_showcase(
            album_id, user_id, body=body, request_options=request_options
        ).unwrap()

    def copy_showcase_alt2(
        self,
        album_id: float,
        *,
        body: MeAlbumsCopyRequest | MeAlbumsCopyRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Album:
        """This method creates a copy of the specified showcase.

        Args:
            album_id: The ID of the showcase.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The copied showcase was created.

        Raises:
            ApiError: The authenticated user can't copy this showcase. No such showcase exists. ``error`` is
                ``LegacyError | RawError``."""
        return self._with_raw_response.copy_showcase_alt2(album_id, body=body, request_options=request_options).unwrap()

    def create_showcase(
        self,
        user_id: float,
        body: UsersAlbumsRequest | UsersAlbumsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Album:
        """This method creates a new showcase for the specified user.

        Args:
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The showcase was created.

        Raises:
            ApiError: A parameter is invalid. The supplied token doesn't have the proper scopes, or the authenticated
                user can't create showcases. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.create_showcase(user_id, body, request_options=request_options).unwrap()

    def create_showcase_alt1(
        self, body: MeAlbumsRequest | MeAlbumsRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> Album:
        """This method creates a new showcase for the specified user.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The showcase was created.

        Raises:
            ApiError: A parameter is invalid. The supplied token doesn't have the proper scopes, or the authenticated
                user can't create showcases. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.create_showcase_alt1(body, request_options=request_options).unwrap()

    def delete_showcase(
        self, album_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes the specified showcase. The authenticated user must be the owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The showcase was deleted.

        Raises:
            ApiError: The supplied token doesn't have the proper scopes, or the authenticated user can't delete the
                showcase. No such showcase exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.delete_showcase(album_id, user_id, request_options=request_options).unwrap()

    def delete_showcase_alt2(self, album_id: float, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """This method deletes the specified showcase. The authenticated user must be the owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The showcase was deleted.

        Raises:
            ApiError: The supplied token doesn't have the proper scopes, or the authenticated user can't delete the
                showcase. No such showcase exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.delete_showcase_alt2(album_id, request_options=request_options).unwrap()

    def edit_showcase(
        self,
        album_id: float,
        user_id: float,
        *,
        body: UsersAlbumsRequest1 | UsersAlbumsRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Album:
        """This method edits the specified showcase. The authenticated user must be the owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The showcase was edited.

        Raises:
            ApiError: A parameter is invalid. The authenticated user doesn't own the showcase, the supplied token
                doesn't have the proper scopes, or the authenticated user can't edit the showcase. No such showcase
                exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.edit_showcase(
            album_id, user_id, body=body, request_options=request_options
        ).unwrap()

    def edit_showcase_alt2(
        self,
        album_id: float,
        *,
        body: MeAlbumsRequest1 | MeAlbumsRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Album:
        """This method edits the specified showcase. The authenticated user must be the owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The showcase was edited.

        Raises:
            ApiError: A parameter is invalid. The authenticated user doesn't own the showcase, the supplied token
                doesn't have the proper scopes, or the authenticated user can't edit the showcase. No such showcase
                exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.edit_showcase_alt2(album_id, body=body, request_options=request_options).unwrap()

    def get_showcase(
        self, album_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Album:
        """This method returns the specified showcase. The authenticated user must be the owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The showcase was returned.

        Raises:
            ApiError: No such showcase exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.get_showcase(album_id, user_id, request_options=request_options).unwrap()

    def get_showcase_alt2(self, album_id: float, *, request_options: RequestOptionsOrDict | None = None) -> Album:
        """This method returns the specified showcase. The authenticated user must be the owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The showcase was returned.

        Raises:
            ApiError: No such showcase exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.get_showcase_alt2(album_id, request_options=request_options).unwrap()

    def get_showcases(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter_privacy: str | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort18OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AlbumConnection:
        """This method returns every showcase belonging to the authenticated user.

        Args:
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_privacy: A comma-separated list of showcase privacies to include. Valid options are ``anybody`` for
                universal access, ``password`` for password-restricted access, ``embed_only`` for restricted access on
                Vimeo but available as an embedded showcase elsewhere, ``team`` for team-only access, ``nobody`` for
                owner-only access, and ``unlisted`` for restricted access except for those with a direct link. By
                default, all privacies are returned.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date of creation. * ``duration`` - Sort the results by
                duration. * ``last_modified`` - Sort the results by last modified date. * ``videos`` - Sort the results
                by the number of videos.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The showcases were returned.

        Raises:
            ApiError: A parameter is invalid. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.get_showcases(
            user_id,
            direction=direction,
            filter_privacy=filter_privacy,
            page=page,
            per_page=per_page,
            query=query,
            sort=sort,
            request_options=request_options,
        ).unwrap()

    def get_showcases_alt1(
        self,
        *,
        direction: DirectionOrStr | None = None,
        filter_privacy: str | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort18OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AlbumConnection:
        """This method returns every showcase belonging to the authenticated user.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_privacy: A comma-separated list of showcase privacies to include. Valid options are ``anybody`` for
                universal access, ``password`` for password-restricted access, ``embed_only`` for restricted access on
                Vimeo but available as an embedded showcase elsewhere, ``team`` for team-only access, ``nobody`` for
                owner-only access, and ``unlisted`` for restricted access except for those with a direct link. By
                default, all privacies are returned.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date of creation. * ``duration`` - Sort the results by
                duration. * ``last_modified`` - Sort the results by last modified date. * ``videos`` - Sort the results
                by the number of videos.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The showcases were returned.

        Raises:
            ApiError: A parameter is invalid. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.get_showcases_alt1(
            direction=direction,
            filter_privacy=filter_privacy,
            page=page,
            per_page=per_page,
            query=query,
            sort=sort,
            request_options=request_options,
        ).unwrap()

    def update_showcases(
        self,
        user_id: float,
        album_item_uris: str,
        album_uris: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method adds videos and events to the specified showcases. The authenticated user must either be the
        owner of the showcase or have team permissions.

        The present setup permits only one event per showcase.

        Args:
            user_id: The ID of the user.
            album_item_uris: A comma-separated list of video or event URIs.
            album_uris: A comma-separated list of showcase URIs.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos and events were added to the showcases.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_showcases(
            user_id, album_item_uris, album_uris, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> ShowcasesEssentialsWithRawResponse:
        return self._with_raw_response


class AsyncShowcasesEssentials:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncShowcasesEssentialsWithRawResponse(client, server, auth)

    async def add_folder_to_showcases(
        self, user_id: float, album_uris: str, folder_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method adds all videos and events from a specified folder to showcases.

        The authenticated user must either be the owner of the showcase or have team permissions.

        Args:
            user_id: The ID of the user.
            album_uris: A comma-separated list of showcase URIs.
            folder_id: The ID of the folder containing videos and events to add.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The folder contents were added to the showcases.

        Raises:
            ApiError: Error code 2204: A parameter is invalid. Error code 3200: The user lacks the permissions to update
                the showcases or access the folder. Error code 5000: The folder was not found. ``error`` is ``Error |
                RawError``."""
        return (
            await self._with_raw_response.add_folder_to_showcases(
                user_id, album_uris, folder_id, request_options=request_options
            )
        ).unwrap()

    async def copy_showcase(
        self,
        album_id: float,
        user_id: float,
        *,
        body: UsersAlbumsCopyRequest | UsersAlbumsCopyRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Album:
        """This method creates a copy of the specified showcase.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The copied showcase was created.

        Raises:
            ApiError: The authenticated user can't copy this showcase. No such showcase exists. ``error`` is
                ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.copy_showcase(album_id, user_id, body=body, request_options=request_options)
        ).unwrap()

    async def copy_showcase_alt2(
        self,
        album_id: float,
        *,
        body: MeAlbumsCopyRequest | MeAlbumsCopyRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Album:
        """This method creates a copy of the specified showcase.

        Args:
            album_id: The ID of the showcase.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The copied showcase was created.

        Raises:
            ApiError: The authenticated user can't copy this showcase. No such showcase exists. ``error`` is
                ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.copy_showcase_alt2(album_id, body=body, request_options=request_options)
        ).unwrap()

    async def create_showcase(
        self,
        user_id: float,
        body: UsersAlbumsRequest | UsersAlbumsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Album:
        """This method creates a new showcase for the specified user.

        Args:
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The showcase was created.

        Raises:
            ApiError: A parameter is invalid. The supplied token doesn't have the proper scopes, or the authenticated
                user can't create showcases. ``error`` is ``LegacyError | RawError``."""
        return (await self._with_raw_response.create_showcase(user_id, body, request_options=request_options)).unwrap()

    async def create_showcase_alt1(
        self, body: MeAlbumsRequest | MeAlbumsRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> Album:
        """This method creates a new showcase for the specified user.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The showcase was created.

        Raises:
            ApiError: A parameter is invalid. The supplied token doesn't have the proper scopes, or the authenticated
                user can't create showcases. ``error`` is ``LegacyError | RawError``."""
        return (await self._with_raw_response.create_showcase_alt1(body, request_options=request_options)).unwrap()

    async def delete_showcase(
        self, album_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes the specified showcase. The authenticated user must be the owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The showcase was deleted.

        Raises:
            ApiError: The supplied token doesn't have the proper scopes, or the authenticated user can't delete the
                showcase. No such showcase exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.delete_showcase(album_id, user_id, request_options=request_options)
        ).unwrap()

    async def delete_showcase_alt2(
        self, album_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes the specified showcase. The authenticated user must be the owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The showcase was deleted.

        Raises:
            ApiError: The supplied token doesn't have the proper scopes, or the authenticated user can't delete the
                showcase. No such showcase exists. ``error`` is ``LegacyError | RawError``."""
        return (await self._with_raw_response.delete_showcase_alt2(album_id, request_options=request_options)).unwrap()

    async def edit_showcase(
        self,
        album_id: float,
        user_id: float,
        *,
        body: UsersAlbumsRequest1 | UsersAlbumsRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Album:
        """This method edits the specified showcase. The authenticated user must be the owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The showcase was edited.

        Raises:
            ApiError: A parameter is invalid. The authenticated user doesn't own the showcase, the supplied token
                doesn't have the proper scopes, or the authenticated user can't edit the showcase. No such showcase
                exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.edit_showcase(album_id, user_id, body=body, request_options=request_options)
        ).unwrap()

    async def edit_showcase_alt2(
        self,
        album_id: float,
        *,
        body: MeAlbumsRequest1 | MeAlbumsRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Album:
        """This method edits the specified showcase. The authenticated user must be the owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The showcase was edited.

        Raises:
            ApiError: A parameter is invalid. The authenticated user doesn't own the showcase, the supplied token
                doesn't have the proper scopes, or the authenticated user can't edit the showcase. No such showcase
                exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.edit_showcase_alt2(album_id, body=body, request_options=request_options)
        ).unwrap()

    async def get_showcase(
        self, album_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Album:
        """This method returns the specified showcase. The authenticated user must be the owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The showcase was returned.

        Raises:
            ApiError: No such showcase exists. ``error`` is ``LegacyError | RawError``."""
        return (await self._with_raw_response.get_showcase(album_id, user_id, request_options=request_options)).unwrap()

    async def get_showcase_alt2(self, album_id: float, *, request_options: RequestOptionsOrDict | None = None) -> Album:
        """This method returns the specified showcase. The authenticated user must be the owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The showcase was returned.

        Raises:
            ApiError: No such showcase exists. ``error`` is ``LegacyError | RawError``."""
        return (await self._with_raw_response.get_showcase_alt2(album_id, request_options=request_options)).unwrap()

    async def get_showcases(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter_privacy: str | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort18OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AlbumConnection:
        """This method returns every showcase belonging to the authenticated user.

        Args:
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_privacy: A comma-separated list of showcase privacies to include. Valid options are ``anybody`` for
                universal access, ``password`` for password-restricted access, ``embed_only`` for restricted access on
                Vimeo but available as an embedded showcase elsewhere, ``team`` for team-only access, ``nobody`` for
                owner-only access, and ``unlisted`` for restricted access except for those with a direct link. By
                default, all privacies are returned.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date of creation. * ``duration`` - Sort the results by
                duration. * ``last_modified`` - Sort the results by last modified date. * ``videos`` - Sort the results
                by the number of videos.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The showcases were returned.

        Raises:
            ApiError: A parameter is invalid. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.get_showcases(
                user_id,
                direction=direction,
                filter_privacy=filter_privacy,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                request_options=request_options,
            )
        ).unwrap()

    async def get_showcases_alt1(
        self,
        *,
        direction: DirectionOrStr | None = None,
        filter_privacy: str | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort18OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AlbumConnection:
        """This method returns every showcase belonging to the authenticated user.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_privacy: A comma-separated list of showcase privacies to include. Valid options are ``anybody`` for
                universal access, ``password`` for password-restricted access, ``embed_only`` for restricted access on
                Vimeo but available as an embedded showcase elsewhere, ``team`` for team-only access, ``nobody`` for
                owner-only access, and ``unlisted`` for restricted access except for those with a direct link. By
                default, all privacies are returned.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date of creation. * ``duration`` - Sort the results by
                duration. * ``last_modified`` - Sort the results by last modified date. * ``videos`` - Sort the results
                by the number of videos.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The showcases were returned.

        Raises:
            ApiError: A parameter is invalid. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.get_showcases_alt1(
                direction=direction,
                filter_privacy=filter_privacy,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                request_options=request_options,
            )
        ).unwrap()

    async def update_showcases(
        self,
        user_id: float,
        album_item_uris: str,
        album_uris: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method adds videos and events to the specified showcases. The authenticated user must either be the
        owner of the showcase or have team permissions.

        The present setup permits only one event per showcase.

        Args:
            user_id: The ID of the user.
            album_item_uris: A comma-separated list of video or event URIs.
            album_uris: A comma-separated list of showcase URIs.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos and events were added to the showcases.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_showcases(
                user_id, album_item_uris, album_uris, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncShowcasesEssentialsWithRawResponse:
        return self._with_raw_response


class ShowcasesEssentialsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def add_folder_to_showcases(
        self, user_id: float, album_uris: str, folder_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, AddFolderToShowcasesErrorBody]:
        """This method adds all videos and events from a specified folder to showcases.

        The authenticated user must either be the owner of the showcase or have team permissions.

        Args:
            user_id: The ID of the user.
            album_uris: A comma-separated list of showcase URIs.
            folder_id: The ID of the folder containing videos and events to add.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/users/{user_id}/albums/from_folder"),
            path_params=[param[float]("user_id", user_id)],
            query_params=[param[str]("album_uris", album_uris), param[float]("folder_id", folder_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=add_folder_to_showcases_error_mapper,
            request_options=request_options,
        )

    def copy_showcase(
        self,
        album_id: float,
        user_id: float,
        *,
        body: UsersAlbumsCopyRequest | UsersAlbumsCopyRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Album, CopyShowcaseErrorBody]:
        """This method creates a copy of the specified showcase.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users/{user_id}/albums/{album_id}/copy"),
            path_params=[param[float]("album_id", album_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersAlbumsCopyRequest | UsersAlbumsCopyRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Album],
            error_mapper=copy_showcase_error_mapper,
            request_options=request_options,
        )

    def copy_showcase_alt2(
        self,
        album_id: float,
        *,
        body: MeAlbumsCopyRequest | MeAlbumsCopyRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Album, CopyShowcaseAlt2ErrorBody]:
        """This method creates a copy of the specified showcase.

        Args:
            album_id: The ID of the showcase.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/me/albums/{album_id}/copy"),
            path_params=[param[float]("album_id", album_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MeAlbumsCopyRequest | MeAlbumsCopyRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Album],
            error_mapper=copy_showcase_alt2_error_mapper,
            request_options=request_options,
        )

    def create_showcase(
        self,
        user_id: float,
        body: UsersAlbumsRequest | UsersAlbumsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Album, CreateShowcaseErrorBody]:
        """This method creates a new showcase for the specified user.

        Args:
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users/{user_id}/albums"),
            path_params=[param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersAlbumsRequest | UsersAlbumsRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Album],
            error_mapper=create_showcase_error_mapper,
            request_options=request_options,
        )

    def create_showcase_alt1(
        self, body: MeAlbumsRequest | MeAlbumsRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Album, CreateShowcaseAlt1ErrorBody]:
        """This method creates a new showcase for the specified user.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/me/albums"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MeAlbumsRequest | MeAlbumsRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Album],
            error_mapper=create_showcase_alt1_error_mapper,
            request_options=request_options,
        )

    def delete_showcase(
        self, album_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteShowcaseErrorBody]:
        """This method deletes the specified showcase. The authenticated user must be the owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/users/{user_id}/albums/{album_id}"),
            path_params=[param[float]("album_id", album_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_showcase_error_mapper,
            request_options=request_options,
        )

    def delete_showcase_alt2(
        self, album_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteShowcaseAlt2ErrorBody]:
        """This method deletes the specified showcase. The authenticated user must be the owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/albums/{album_id}"),
            path_params=[param[float]("album_id", album_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_showcase_alt2_error_mapper,
            request_options=request_options,
        )

    def edit_showcase(
        self,
        album_id: float,
        user_id: float,
        *,
        body: UsersAlbumsRequest1 | UsersAlbumsRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Album, EditShowcaseErrorBody]:
        """This method edits the specified showcase. The authenticated user must be the owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/users/{user_id}/albums/{album_id}"),
            path_params=[param[float]("album_id", album_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersAlbumsRequest1 | UsersAlbumsRequest1Dict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Album],
            error_mapper=edit_showcase_error_mapper,
            request_options=request_options,
        )

    def edit_showcase_alt2(
        self,
        album_id: float,
        *,
        body: MeAlbumsRequest1 | MeAlbumsRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Album, EditShowcaseAlt2ErrorBody]:
        """This method edits the specified showcase. The authenticated user must be the owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/me/albums/{album_id}"),
            path_params=[param[float]("album_id", album_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MeAlbumsRequest1 | MeAlbumsRequest1Dict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Album],
            error_mapper=edit_showcase_alt2_error_mapper,
            request_options=request_options,
        )

    def get_showcase(
        self, album_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Album, GetShowcaseErrorBody]:
        """This method returns the specified showcase. The authenticated user must be the owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/albums/{album_id}"),
            path_params=[param[float]("album_id", album_id), param[float]("user_id", user_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Album],
            error_mapper=get_showcase_error_mapper,
            request_options=request_options,
        )

    def get_showcase_alt2(
        self, album_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Album, GetShowcaseAlt2ErrorBody]:
        """This method returns the specified showcase. The authenticated user must be the owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/albums/{album_id}"),
            path_params=[param[float]("album_id", album_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Album],
            error_mapper=get_showcase_alt2_error_mapper,
            request_options=request_options,
        )

    def get_showcases(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter_privacy: str | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort18OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AlbumConnection, GetShowcasesErrorBody]:
        """This method returns every showcase belonging to the authenticated user.

        Args:
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_privacy: A comma-separated list of showcase privacies to include. Valid options are ``anybody`` for
                universal access, ``password`` for password-restricted access, ``embed_only`` for restricted access on
                Vimeo but available as an embedded showcase elsewhere, ``team`` for team-only access, ``nobody`` for
                owner-only access, and ``unlisted`` for restricted access except for those with a direct link. By
                default, all privacies are returned.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date of creation. * ``duration`` - Sort the results by
                duration. * ``last_modified`` - Sort the results by last modified date. * ``videos`` - Sort the results
                by the number of videos.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/albums"),
            path_params=[param[float]("user_id", user_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[str | None]("filter_privacy", filter_privacy),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort18OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[AlbumConnection],
            error_mapper=get_showcases_error_mapper,
            request_options=request_options,
        )

    def get_showcases_alt1(
        self,
        *,
        direction: DirectionOrStr | None = None,
        filter_privacy: str | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort18OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AlbumConnection, GetShowcasesAlt1ErrorBody]:
        """This method returns every showcase belonging to the authenticated user.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_privacy: A comma-separated list of showcase privacies to include. Valid options are ``anybody`` for
                universal access, ``password`` for password-restricted access, ``embed_only`` for restricted access on
                Vimeo but available as an embedded showcase elsewhere, ``team`` for team-only access, ``nobody`` for
                owner-only access, and ``unlisted`` for restricted access except for those with a direct link. By
                default, all privacies are returned.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date of creation. * ``duration`` - Sort the results by
                duration. * ``last_modified`` - Sort the results by last modified date. * ``videos`` - Sort the results
                by the number of videos.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/albums"),
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[str | None]("filter_privacy", filter_privacy),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort18OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[AlbumConnection],
            error_mapper=get_showcases_alt1_error_mapper,
            request_options=request_options,
        )

    def update_showcases(
        self,
        user_id: float,
        album_item_uris: str,
        album_uris: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """This method adds videos and events to the specified showcases. The authenticated user must either be the
        owner of the showcase or have team permissions.

        The present setup permits only one event per showcase.

        Args:
            user_id: The ID of the user.
            album_item_uris: A comma-separated list of video or event URIs.
            album_uris: A comma-separated list of showcase URIs.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/users/{user_id}/albums"),
            path_params=[param[float]("user_id", user_id)],
            query_params=[param[str]("album_item_uris", album_item_uris), param[str]("album_uris", album_uris)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncShowcasesEssentialsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def add_folder_to_showcases(
        self, user_id: float, album_uris: str, folder_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, AddFolderToShowcasesErrorBody]:
        """This method adds all videos and events from a specified folder to showcases.

        The authenticated user must either be the owner of the showcase or have team permissions.

        Args:
            user_id: The ID of the user.
            album_uris: A comma-separated list of showcase URIs.
            folder_id: The ID of the folder containing videos and events to add.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/users/{user_id}/albums/from_folder"),
            path_params=[param[float]("user_id", user_id)],
            query_params=[param[str]("album_uris", album_uris), param[float]("folder_id", folder_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=add_folder_to_showcases_error_mapper,
            request_options=request_options,
        )

    async def copy_showcase(
        self,
        album_id: float,
        user_id: float,
        *,
        body: UsersAlbumsCopyRequest | UsersAlbumsCopyRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Album, CopyShowcaseErrorBody]:
        """This method creates a copy of the specified showcase.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users/{user_id}/albums/{album_id}/copy"),
            path_params=[param[float]("album_id", album_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersAlbumsCopyRequest | UsersAlbumsCopyRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Album],
            error_mapper=copy_showcase_error_mapper,
            request_options=request_options,
        )

    async def copy_showcase_alt2(
        self,
        album_id: float,
        *,
        body: MeAlbumsCopyRequest | MeAlbumsCopyRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Album, CopyShowcaseAlt2ErrorBody]:
        """This method creates a copy of the specified showcase.

        Args:
            album_id: The ID of the showcase.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/me/albums/{album_id}/copy"),
            path_params=[param[float]("album_id", album_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MeAlbumsCopyRequest | MeAlbumsCopyRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Album],
            error_mapper=copy_showcase_alt2_error_mapper,
            request_options=request_options,
        )

    async def create_showcase(
        self,
        user_id: float,
        body: UsersAlbumsRequest | UsersAlbumsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Album, CreateShowcaseErrorBody]:
        """This method creates a new showcase for the specified user.

        Args:
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users/{user_id}/albums"),
            path_params=[param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersAlbumsRequest | UsersAlbumsRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Album],
            error_mapper=create_showcase_error_mapper,
            request_options=request_options,
        )

    async def create_showcase_alt1(
        self, body: MeAlbumsRequest | MeAlbumsRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Album, CreateShowcaseAlt1ErrorBody]:
        """This method creates a new showcase for the specified user.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/me/albums"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MeAlbumsRequest | MeAlbumsRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Album],
            error_mapper=create_showcase_alt1_error_mapper,
            request_options=request_options,
        )

    async def delete_showcase(
        self, album_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteShowcaseErrorBody]:
        """This method deletes the specified showcase. The authenticated user must be the owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/users/{user_id}/albums/{album_id}"),
            path_params=[param[float]("album_id", album_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_showcase_error_mapper,
            request_options=request_options,
        )

    async def delete_showcase_alt2(
        self, album_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteShowcaseAlt2ErrorBody]:
        """This method deletes the specified showcase. The authenticated user must be the owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/albums/{album_id}"),
            path_params=[param[float]("album_id", album_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_showcase_alt2_error_mapper,
            request_options=request_options,
        )

    async def edit_showcase(
        self,
        album_id: float,
        user_id: float,
        *,
        body: UsersAlbumsRequest1 | UsersAlbumsRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Album, EditShowcaseErrorBody]:
        """This method edits the specified showcase. The authenticated user must be the owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/users/{user_id}/albums/{album_id}"),
            path_params=[param[float]("album_id", album_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersAlbumsRequest1 | UsersAlbumsRequest1Dict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Album],
            error_mapper=edit_showcase_error_mapper,
            request_options=request_options,
        )

    async def edit_showcase_alt2(
        self,
        album_id: float,
        *,
        body: MeAlbumsRequest1 | MeAlbumsRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Album, EditShowcaseAlt2ErrorBody]:
        """This method edits the specified showcase. The authenticated user must be the owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/me/albums/{album_id}"),
            path_params=[param[float]("album_id", album_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MeAlbumsRequest1 | MeAlbumsRequest1Dict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Album],
            error_mapper=edit_showcase_alt2_error_mapper,
            request_options=request_options,
        )

    async def get_showcase(
        self, album_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Album, GetShowcaseErrorBody]:
        """This method returns the specified showcase. The authenticated user must be the owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/albums/{album_id}"),
            path_params=[param[float]("album_id", album_id), param[float]("user_id", user_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Album],
            error_mapper=get_showcase_error_mapper,
            request_options=request_options,
        )

    async def get_showcase_alt2(
        self, album_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Album, GetShowcaseAlt2ErrorBody]:
        """This method returns the specified showcase. The authenticated user must be the owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/albums/{album_id}"),
            path_params=[param[float]("album_id", album_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Album],
            error_mapper=get_showcase_alt2_error_mapper,
            request_options=request_options,
        )

    async def get_showcases(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter_privacy: str | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort18OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AlbumConnection, GetShowcasesErrorBody]:
        """This method returns every showcase belonging to the authenticated user.

        Args:
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_privacy: A comma-separated list of showcase privacies to include. Valid options are ``anybody`` for
                universal access, ``password`` for password-restricted access, ``embed_only`` for restricted access on
                Vimeo but available as an embedded showcase elsewhere, ``team`` for team-only access, ``nobody`` for
                owner-only access, and ``unlisted`` for restricted access except for those with a direct link. By
                default, all privacies are returned.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date of creation. * ``duration`` - Sort the results by
                duration. * ``last_modified`` - Sort the results by last modified date. * ``videos`` - Sort the results
                by the number of videos.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/albums"),
            path_params=[param[float]("user_id", user_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[str | None]("filter_privacy", filter_privacy),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort18OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[AlbumConnection],
            error_mapper=get_showcases_error_mapper,
            request_options=request_options,
        )

    async def get_showcases_alt1(
        self,
        *,
        direction: DirectionOrStr | None = None,
        filter_privacy: str | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort18OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AlbumConnection, GetShowcasesAlt1ErrorBody]:
        """This method returns every showcase belonging to the authenticated user.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_privacy: A comma-separated list of showcase privacies to include. Valid options are ``anybody`` for
                universal access, ``password`` for password-restricted access, ``embed_only`` for restricted access on
                Vimeo but available as an embedded showcase elsewhere, ``team`` for team-only access, ``nobody`` for
                owner-only access, and ``unlisted`` for restricted access except for those with a direct link. By
                default, all privacies are returned.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date of creation. * ``duration`` - Sort the results by
                duration. * ``last_modified`` - Sort the results by last modified date. * ``videos`` - Sort the results
                by the number of videos.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/albums"),
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[str | None]("filter_privacy", filter_privacy),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort18OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[AlbumConnection],
            error_mapper=get_showcases_alt1_error_mapper,
            request_options=request_options,
        )

    async def update_showcases(
        self,
        user_id: float,
        album_item_uris: str,
        album_uris: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """This method adds videos and events to the specified showcases. The authenticated user must either be the
        owner of the showcase or have team permissions.

        The present setup permits only one event per showcase.

        Args:
            user_id: The ID of the user.
            album_item_uris: A comma-separated list of video or event URIs.
            album_uris: A comma-separated list of showcase URIs.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/users/{user_id}/albums"),
            path_params=[param[float]("user_id", user_id)],
            query_params=[param[str]("album_item_uris", album_item_uris), param[str]("album_uris", album_uris)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )
