from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AnySchemes,
    ApiResult,
    AsyncAnySchemes,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_empty_response,
    async_json_decoder,
    empty_response,
    json_body,
    json_decoder,
    param,
    unwrap,
)
from ..errors.create_project_alt1_error import CreateProjectAlt1ErrorBody, create_project_alt1_error_mapper
from ..errors.create_project_error import CreateProjectErrorBody, create_project_error_mapper
from ..errors.delete_project_alt1_error import DeleteProjectAlt1ErrorBody, delete_project_alt1_error_mapper
from ..errors.delete_project_error import DeleteProjectErrorBody, delete_project_error_mapper
from ..errors.edit_project_alt1_error import EditProjectAlt1ErrorBody, edit_project_alt1_error_mapper
from ..errors.edit_project_error import EditProjectErrorBody, edit_project_error_mapper
from ..errors.get_private_to_me_folder_error import GetPrivateToMeFolderErrorBody, get_private_to_me_folder_error_mapper
from ..errors.get_project_alt1_error import GetProjectAlt1ErrorBody, get_project_alt1_error_mapper
from ..errors.get_project_error import GetProjectErrorBody, get_project_error_mapper
from ..errors.get_projects_alt1_error import GetProjectsAlt1ErrorBody, get_projects_alt1_error_mapper
from ..errors.get_projects_error import GetProjectsErrorBody, get_projects_error_mapper
from ..models.enums.direction import DirectionOrStr
from ..models.enums.sort36 import Sort36OrStr
from ..models.me_projects_request import MeProjectsRequest, MeProjectsRequestDict
from ..models.me_projects_request1 import MeProjectsRequest1, MeProjectsRequest1Dict
from ..models.me_projects_request2 import MeProjectsRequest2, MeProjectsRequest2Dict
from ..models.project import Project
from ..models.project_connection import ProjectConnection
from ..models.users_projects_request import UsersProjectsRequest, UsersProjectsRequestDict
from ..models.users_projects_request1 import UsersProjectsRequest1, UsersProjectsRequest1Dict
from ..models.users_projects_request2 import UsersProjectsRequest2, UsersProjectsRequest2Dict
from ..server.server import Server


class FoldersEssentials:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = FoldersEssentialsWithRawResponse(client, server, auth)

    def create_project(
        self,
        user_id: float,
        body: UsersProjectsRequest | UsersProjectsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Project:
        """This method creates a new folder for the authenticated user. By default, this method creates a top-level
        folder. To create a subfolder — that is, to place the new folder inside an existing folder — specify the parent
        folder by URI with the **parent_folder_uri** parameter in the body of the request.

        Args:
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The folder was created.

        Raises:
            ApiError: * Error code 2204: The input is invalid. * Error code 2205: The input is empty. Error code 8000:
                The user credentials are invalid. * Error code 3200: The authenticated user can't create folders. *
                Error code 3701: The maximum folder depth has been exceeded. ``error`` is ``Error | RawError``."""
        return unwrap(self._with_raw_response.create_project(user_id, body, request_options=request_options))

    def create_project_alt1(
        self, body: MeProjectsRequest | MeProjectsRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> Project:
        """This method creates a new folder for the authenticated user. By default, this method creates a top-level
        folder. To create a subfolder — that is, to place the new folder inside an existing folder — specify the parent
        folder by URI with the **parent_folder_uri** parameter in the body of the request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The folder was created.

        Raises:
            ApiError: * Error code 2204: The input is invalid. * Error code 2205: The input is empty. Error code 8000:
                The user credentials are invalid. * Error code 3200: The authenticated user can't create folders. *
                Error code 3701: The maximum folder depth has been exceeded. ``error`` is ``Error | RawError``."""
        return unwrap(self._with_raw_response.create_project_alt1(body, request_options=request_options))

    def delete_project(
        self,
        project_id: float,
        user_id: float,
        *,
        body: UsersProjectsRequest1 | UsersProjectsRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method deletes the specified folder and optionally also the videos that it contains. The authenticated
        user must be the owner of the folder.

        Args:
            project_id: The ID of the folder.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The folder was deleted.

        Raises:
            ApiError: Error code 8000: The user credentials are invalid. Error code 3200: The authenticated user can't
                delete the folder. Error code 5000: No such folder exists. ``error`` is ``Error | RawError``."""
        return unwrap(
            self._with_raw_response.delete_project(project_id, user_id, body=body, request_options=request_options)
        )

    def delete_project_alt1(
        self,
        project_id: float,
        *,
        body: MeProjectsRequest1 | MeProjectsRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method deletes the specified folder and optionally also the videos that it contains. The authenticated
        user must be the owner of the folder.

        Args:
            project_id: The ID of the folder.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The folder was deleted.

        Raises:
            ApiError: Error code 8000: The user credentials are invalid. Error code 3200: The authenticated user can't
                delete the folder. Error code 5000: No such folder exists. ``error`` is ``Error | RawError``."""
        return unwrap(
            self._with_raw_response.delete_project_alt1(project_id, body=body, request_options=request_options)
        )

    def edit_project(
        self,
        project_id: float,
        user_id: float,
        body: UsersProjectsRequest2 | UsersProjectsRequest2Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Project:
        """This method edits the specified folder. The authenticated user must be the owner of the folder.

        Args:
            project_id: The ID of the folder.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The folder was edited.

        Raises:
            ApiError: * Error code 2204: The input is invalid. * Error code 2205: The input is empty. Error code 8000:
                The user credentials are invalid. * Error code 3200: The authenticated user can't edit the folder. *
                Error code 3449: The authenticated user can't edit folder settings. * Error code 3702: Folder settings
                aren't enabled for this team. Error code 5000: No such folder exists. ``error`` is ``Error |
                RawError``."""
        return unwrap(self._with_raw_response.edit_project(project_id, user_id, body, request_options=request_options))

    def edit_project_alt1(
        self,
        project_id: float,
        body: MeProjectsRequest2 | MeProjectsRequest2Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Project:
        """This method edits the specified folder. The authenticated user must be the owner of the folder.

        Args:
            project_id: The ID of the folder.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The folder was edited.

        Raises:
            ApiError: * Error code 2204: The input is invalid. * Error code 2205: The input is empty. Error code 8000:
                The user credentials are invalid. * Error code 3200: The authenticated user can't edit the folder. *
                Error code 3449: The authenticated user can't edit folder settings. * Error code 3702: Folder settings
                aren't enabled for this team. Error code 5000: No such folder exists. ``error`` is ``Error |
                RawError``."""
        return unwrap(self._with_raw_response.edit_project_alt1(project_id, body, request_options=request_options))

    def get_private_to_me_folder(
        self, owner_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Project:
        """This method returns the specified private-to-me folder.

        Args:
            owner_id: The ID of the owner.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The folder was returned.

        Raises:
            ApiError: Error code 8000: The user credentials are invalid. Error code 5000: No such folder exists.
                ``error`` is ``Error | RawError``."""
        return unwrap(self._with_raw_response.get_private_to_me_folder(owner_id, request_options=request_options))

    def get_project(
        self, project_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Project:
        """This method returns a single folder belonging to the authenticated user.

        Args:
            project_id: The ID of the folder.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The folder was returned.

        Raises:
            ApiError: Error code 8000: The user credentials are invalid. Error code 5000: No such folder exists.
                ``error`` is ``Error | RawError``."""
        return unwrap(self._with_raw_response.get_project(project_id, user_id, request_options=request_options))

    def get_project_alt1(self, project_id: float, *, request_options: RequestOptionsOrDict | None = None) -> Project:
        """This method returns a single folder belonging to the authenticated user.

        Args:
            project_id: The ID of the folder.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The folder was returned.

        Raises:
            ApiError: Error code 8000: The user credentials are invalid. Error code 5000: No such folder exists.
                ``error`` is ``Error | RawError``."""
        return unwrap(self._with_raw_response.get_project_alt1(project_id, request_options=request_options))

    def get_projects(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort36OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProjectConnection:
        """This method returns all the folders belonging to the authenticated user.

        Args:
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``date`` - Sort the results by date. * ``default``
                - Use the default sort order. * ``modified_time`` - Sort the results by last modification. * ``name`` -
                Sort the results by name. * ``pinned_on`` - Sort the results by pinned timestamp.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The folders were returned.

        Raises:
            ApiError: Error code 8000: The user credentials are invalid. ``error`` is ``Error | RawError``."""
        return unwrap(
            self._with_raw_response.get_projects(
                user_id,
                direction=direction,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                request_options=request_options,
            ),
        )

    def get_projects_alt1(
        self,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort36OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProjectConnection:
        """This method returns all the folders belonging to the authenticated user.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``date`` - Sort the results by date. * ``default``
                - Use the default sort order. * ``modified_time`` - Sort the results by last modification. * ``name`` -
                Sort the results by name. * ``pinned_on`` - Sort the results by pinned timestamp.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The folders were returned.

        Raises:
            ApiError: Error code 8000: The user credentials are invalid. ``error`` is ``Error | RawError``."""
        return unwrap(
            self._with_raw_response.get_projects_alt1(
                direction=direction,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> FoldersEssentialsWithRawResponse:
        return self._with_raw_response


class AsyncFoldersEssentials:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncFoldersEssentialsWithRawResponse(client, server, auth)

    async def create_project(
        self,
        user_id: float,
        body: UsersProjectsRequest | UsersProjectsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Project:
        """This method creates a new folder for the authenticated user. By default, this method creates a top-level
        folder. To create a subfolder — that is, to place the new folder inside an existing folder — specify the parent
        folder by URI with the **parent_folder_uri** parameter in the body of the request.

        Args:
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The folder was created.

        Raises:
            ApiError: * Error code 2204: The input is invalid. * Error code 2205: The input is empty. Error code 8000:
                The user credentials are invalid. * Error code 3200: The authenticated user can't create folders. *
                Error code 3701: The maximum folder depth has been exceeded. ``error`` is ``Error | RawError``."""
        return unwrap(await self._with_raw_response.create_project(user_id, body, request_options=request_options))

    async def create_project_alt1(
        self, body: MeProjectsRequest | MeProjectsRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> Project:
        """This method creates a new folder for the authenticated user. By default, this method creates a top-level
        folder. To create a subfolder — that is, to place the new folder inside an existing folder — specify the parent
        folder by URI with the **parent_folder_uri** parameter in the body of the request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The folder was created.

        Raises:
            ApiError: * Error code 2204: The input is invalid. * Error code 2205: The input is empty. Error code 8000:
                The user credentials are invalid. * Error code 3200: The authenticated user can't create folders. *
                Error code 3701: The maximum folder depth has been exceeded. ``error`` is ``Error | RawError``."""
        return unwrap(await self._with_raw_response.create_project_alt1(body, request_options=request_options))

    async def delete_project(
        self,
        project_id: float,
        user_id: float,
        *,
        body: UsersProjectsRequest1 | UsersProjectsRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method deletes the specified folder and optionally also the videos that it contains. The authenticated
        user must be the owner of the folder.

        Args:
            project_id: The ID of the folder.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The folder was deleted.

        Raises:
            ApiError: Error code 8000: The user credentials are invalid. Error code 3200: The authenticated user can't
                delete the folder. Error code 5000: No such folder exists. ``error`` is ``Error | RawError``."""
        return unwrap(
            await self._with_raw_response.delete_project(
                project_id, user_id, body=body, request_options=request_options
            ),
        )

    async def delete_project_alt1(
        self,
        project_id: float,
        *,
        body: MeProjectsRequest1 | MeProjectsRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method deletes the specified folder and optionally also the videos that it contains. The authenticated
        user must be the owner of the folder.

        Args:
            project_id: The ID of the folder.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The folder was deleted.

        Raises:
            ApiError: Error code 8000: The user credentials are invalid. Error code 3200: The authenticated user can't
                delete the folder. Error code 5000: No such folder exists. ``error`` is ``Error | RawError``."""
        return unwrap(
            await self._with_raw_response.delete_project_alt1(project_id, body=body, request_options=request_options)
        )

    async def edit_project(
        self,
        project_id: float,
        user_id: float,
        body: UsersProjectsRequest2 | UsersProjectsRequest2Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Project:
        """This method edits the specified folder. The authenticated user must be the owner of the folder.

        Args:
            project_id: The ID of the folder.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The folder was edited.

        Raises:
            ApiError: * Error code 2204: The input is invalid. * Error code 2205: The input is empty. Error code 8000:
                The user credentials are invalid. * Error code 3200: The authenticated user can't edit the folder. *
                Error code 3449: The authenticated user can't edit folder settings. * Error code 3702: Folder settings
                aren't enabled for this team. Error code 5000: No such folder exists. ``error`` is ``Error |
                RawError``."""
        return unwrap(
            await self._with_raw_response.edit_project(project_id, user_id, body, request_options=request_options)
        )

    async def edit_project_alt1(
        self,
        project_id: float,
        body: MeProjectsRequest2 | MeProjectsRequest2Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Project:
        """This method edits the specified folder. The authenticated user must be the owner of the folder.

        Args:
            project_id: The ID of the folder.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The folder was edited.

        Raises:
            ApiError: * Error code 2204: The input is invalid. * Error code 2205: The input is empty. Error code 8000:
                The user credentials are invalid. * Error code 3200: The authenticated user can't edit the folder. *
                Error code 3449: The authenticated user can't edit folder settings. * Error code 3702: Folder settings
                aren't enabled for this team. Error code 5000: No such folder exists. ``error`` is ``Error |
                RawError``."""
        return unwrap(
            await self._with_raw_response.edit_project_alt1(project_id, body, request_options=request_options)
        )

    async def get_private_to_me_folder(
        self, owner_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Project:
        """This method returns the specified private-to-me folder.

        Args:
            owner_id: The ID of the owner.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The folder was returned.

        Raises:
            ApiError: Error code 8000: The user credentials are invalid. Error code 5000: No such folder exists.
                ``error`` is ``Error | RawError``."""
        return unwrap(await self._with_raw_response.get_private_to_me_folder(owner_id, request_options=request_options))

    async def get_project(
        self, project_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Project:
        """This method returns a single folder belonging to the authenticated user.

        Args:
            project_id: The ID of the folder.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The folder was returned.

        Raises:
            ApiError: Error code 8000: The user credentials are invalid. Error code 5000: No such folder exists.
                ``error`` is ``Error | RawError``."""
        return unwrap(await self._with_raw_response.get_project(project_id, user_id, request_options=request_options))

    async def get_project_alt1(
        self, project_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Project:
        """This method returns a single folder belonging to the authenticated user.

        Args:
            project_id: The ID of the folder.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The folder was returned.

        Raises:
            ApiError: Error code 8000: The user credentials are invalid. Error code 5000: No such folder exists.
                ``error`` is ``Error | RawError``."""
        return unwrap(await self._with_raw_response.get_project_alt1(project_id, request_options=request_options))

    async def get_projects(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort36OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProjectConnection:
        """This method returns all the folders belonging to the authenticated user.

        Args:
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``date`` - Sort the results by date. * ``default``
                - Use the default sort order. * ``modified_time`` - Sort the results by last modification. * ``name`` -
                Sort the results by name. * ``pinned_on`` - Sort the results by pinned timestamp.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The folders were returned.

        Raises:
            ApiError: Error code 8000: The user credentials are invalid. ``error`` is ``Error | RawError``."""
        return unwrap(
            await self._with_raw_response.get_projects(
                user_id,
                direction=direction,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                request_options=request_options,
            ),
        )

    async def get_projects_alt1(
        self,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort36OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProjectConnection:
        """This method returns all the folders belonging to the authenticated user.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``date`` - Sort the results by date. * ``default``
                - Use the default sort order. * ``modified_time`` - Sort the results by last modification. * ``name`` -
                Sort the results by name. * ``pinned_on`` - Sort the results by pinned timestamp.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The folders were returned.

        Raises:
            ApiError: Error code 8000: The user credentials are invalid. ``error`` is ``Error | RawError``."""
        return unwrap(
            await self._with_raw_response.get_projects_alt1(
                direction=direction,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncFoldersEssentialsWithRawResponse:
        return self._with_raw_response


class FoldersEssentialsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_project(
        self,
        user_id: float,
        body: UsersProjectsRequest | UsersProjectsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Project, CreateProjectErrorBody]:
        """This method creates a new folder for the authenticated user. By default, this method creates a top-level
        folder. To create a subfolder — that is, to place the new folder inside an existing folder — specify the parent
        folder by URI with the **parent_folder_uri** parameter in the body of the request.

        Args:
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users/{user_id}/projects"),
            path_params=[param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersProjectsRequest | UsersProjectsRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Project],
            error_mapper=create_project_error_mapper,
            request_options=request_options,
        )

    def create_project_alt1(
        self, body: MeProjectsRequest | MeProjectsRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Project, CreateProjectAlt1ErrorBody]:
        """This method creates a new folder for the authenticated user. By default, this method creates a top-level
        folder. To create a subfolder — that is, to place the new folder inside an existing folder — specify the parent
        folder by URI with the **parent_folder_uri** parameter in the body of the request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/me/projects"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MeProjectsRequest | MeProjectsRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Project],
            error_mapper=create_project_alt1_error_mapper,
            request_options=request_options,
        )

    def delete_project(
        self,
        project_id: float,
        user_id: float,
        *,
        body: UsersProjectsRequest1 | UsersProjectsRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, DeleteProjectErrorBody]:
        """This method deletes the specified folder and optionally also the videos that it contains. The authenticated
        user must be the owner of the folder.

        Args:
            project_id: The ID of the folder.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/users/{user_id}/projects/{project_id}"),
            path_params=[param[float]("project_id", project_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersProjectsRequest1 | UsersProjectsRequest1Dict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_project_error_mapper,
            request_options=request_options,
        )

    def delete_project_alt1(
        self,
        project_id: float,
        *,
        body: MeProjectsRequest1 | MeProjectsRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, DeleteProjectAlt1ErrorBody]:
        """This method deletes the specified folder and optionally also the videos that it contains. The authenticated
        user must be the owner of the folder.

        Args:
            project_id: The ID of the folder.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/projects/{project_id}"),
            path_params=[param[float]("project_id", project_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MeProjectsRequest1 | MeProjectsRequest1Dict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_project_alt1_error_mapper,
            request_options=request_options,
        )

    def edit_project(
        self,
        project_id: float,
        user_id: float,
        body: UsersProjectsRequest2 | UsersProjectsRequest2Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Project, EditProjectErrorBody]:
        """This method edits the specified folder. The authenticated user must be the owner of the folder.

        Args:
            project_id: The ID of the folder.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/users/{user_id}/projects/{project_id}"),
            path_params=[param[float]("project_id", project_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersProjectsRequest2 | UsersProjectsRequest2Dict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Project],
            error_mapper=edit_project_error_mapper,
            request_options=request_options,
        )

    def edit_project_alt1(
        self,
        project_id: float,
        body: MeProjectsRequest2 | MeProjectsRequest2Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Project, EditProjectAlt1ErrorBody]:
        """This method edits the specified folder. The authenticated user must be the owner of the folder.

        Args:
            project_id: The ID of the folder.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/me/projects/{project_id}"),
            path_params=[param[float]("project_id", project_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MeProjectsRequest2 | MeProjectsRequest2Dict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Project],
            error_mapper=edit_project_alt1_error_mapper,
            request_options=request_options,
        )

    def get_private_to_me_folder(
        self, owner_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Project, GetPrivateToMeFolderErrorBody]:
        """This method returns the specified private-to-me folder.

        Args:
            owner_id: The ID of the owner.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{owner_id}/folders/private_to_me"),
            path_params=[param[float]("owner_id", owner_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Project],
            error_mapper=get_private_to_me_folder_error_mapper,
            request_options=request_options,
        )

    def get_project(
        self, project_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Project, GetProjectErrorBody]:
        """This method returns a single folder belonging to the authenticated user.

        Args:
            project_id: The ID of the folder.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/projects/{project_id}"),
            path_params=[param[float]("project_id", project_id), param[float]("user_id", user_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Project],
            error_mapper=get_project_error_mapper,
            request_options=request_options,
        )

    def get_project_alt1(
        self, project_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Project, GetProjectAlt1ErrorBody]:
        """This method returns a single folder belonging to the authenticated user.

        Args:
            project_id: The ID of the folder.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/projects/{project_id}"),
            path_params=[param[float]("project_id", project_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Project],
            error_mapper=get_project_alt1_error_mapper,
            request_options=request_options,
        )

    def get_projects(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort36OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProjectConnection, GetProjectsErrorBody]:
        """This method returns all the folders belonging to the authenticated user.

        Args:
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``date`` - Sort the results by date. * ``default``
                - Use the default sort order. * ``modified_time`` - Sort the results by last modification. * ``name`` -
                Sort the results by name. * ``pinned_on`` - Sort the results by pinned timestamp.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/projects"),
            path_params=[param[float]("user_id", user_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort36OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[ProjectConnection],
            error_mapper=get_projects_error_mapper,
            request_options=request_options,
        )

    def get_projects_alt1(
        self,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort36OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProjectConnection, GetProjectsAlt1ErrorBody]:
        """This method returns all the folders belonging to the authenticated user.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``date`` - Sort the results by date. * ``default``
                - Use the default sort order. * ``modified_time`` - Sort the results by last modification. * ``name`` -
                Sort the results by name. * ``pinned_on`` - Sort the results by pinned timestamp.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/projects"),
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort36OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[ProjectConnection],
            error_mapper=get_projects_alt1_error_mapper,
            request_options=request_options,
        )


class AsyncFoldersEssentialsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_project(
        self,
        user_id: float,
        body: UsersProjectsRequest | UsersProjectsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Project, CreateProjectErrorBody]:
        """This method creates a new folder for the authenticated user. By default, this method creates a top-level
        folder. To create a subfolder — that is, to place the new folder inside an existing folder — specify the parent
        folder by URI with the **parent_folder_uri** parameter in the body of the request.

        Args:
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users/{user_id}/projects"),
            path_params=[param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersProjectsRequest | UsersProjectsRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Project],
            error_mapper=create_project_error_mapper,
            request_options=request_options,
        )

    async def create_project_alt1(
        self, body: MeProjectsRequest | MeProjectsRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Project, CreateProjectAlt1ErrorBody]:
        """This method creates a new folder for the authenticated user. By default, this method creates a top-level
        folder. To create a subfolder — that is, to place the new folder inside an existing folder — specify the parent
        folder by URI with the **parent_folder_uri** parameter in the body of the request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/me/projects"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MeProjectsRequest | MeProjectsRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Project],
            error_mapper=create_project_alt1_error_mapper,
            request_options=request_options,
        )

    async def delete_project(
        self,
        project_id: float,
        user_id: float,
        *,
        body: UsersProjectsRequest1 | UsersProjectsRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, DeleteProjectErrorBody]:
        """This method deletes the specified folder and optionally also the videos that it contains. The authenticated
        user must be the owner of the folder.

        Args:
            project_id: The ID of the folder.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/users/{user_id}/projects/{project_id}"),
            path_params=[param[float]("project_id", project_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersProjectsRequest1 | UsersProjectsRequest1Dict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_empty_response,
            error_mapper=delete_project_error_mapper,
            request_options=request_options,
        )

    async def delete_project_alt1(
        self,
        project_id: float,
        *,
        body: MeProjectsRequest1 | MeProjectsRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, DeleteProjectAlt1ErrorBody]:
        """This method deletes the specified folder and optionally also the videos that it contains. The authenticated
        user must be the owner of the folder.

        Args:
            project_id: The ID of the folder.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/projects/{project_id}"),
            path_params=[param[float]("project_id", project_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MeProjectsRequest1 | MeProjectsRequest1Dict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_empty_response,
            error_mapper=delete_project_alt1_error_mapper,
            request_options=request_options,
        )

    async def edit_project(
        self,
        project_id: float,
        user_id: float,
        body: UsersProjectsRequest2 | UsersProjectsRequest2Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Project, EditProjectErrorBody]:
        """This method edits the specified folder. The authenticated user must be the owner of the folder.

        Args:
            project_id: The ID of the folder.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/users/{user_id}/projects/{project_id}"),
            path_params=[param[float]("project_id", project_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersProjectsRequest2 | UsersProjectsRequest2Dict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Project],
            error_mapper=edit_project_error_mapper,
            request_options=request_options,
        )

    async def edit_project_alt1(
        self,
        project_id: float,
        body: MeProjectsRequest2 | MeProjectsRequest2Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Project, EditProjectAlt1ErrorBody]:
        """This method edits the specified folder. The authenticated user must be the owner of the folder.

        Args:
            project_id: The ID of the folder.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/me/projects/{project_id}"),
            path_params=[param[float]("project_id", project_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MeProjectsRequest2 | MeProjectsRequest2Dict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Project],
            error_mapper=edit_project_alt1_error_mapper,
            request_options=request_options,
        )

    async def get_private_to_me_folder(
        self, owner_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Project, GetPrivateToMeFolderErrorBody]:
        """This method returns the specified private-to-me folder.

        Args:
            owner_id: The ID of the owner.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{owner_id}/folders/private_to_me"),
            path_params=[param[float]("owner_id", owner_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Project],
            error_mapper=get_private_to_me_folder_error_mapper,
            request_options=request_options,
        )

    async def get_project(
        self, project_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Project, GetProjectErrorBody]:
        """This method returns a single folder belonging to the authenticated user.

        Args:
            project_id: The ID of the folder.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/projects/{project_id}"),
            path_params=[param[float]("project_id", project_id), param[float]("user_id", user_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Project],
            error_mapper=get_project_error_mapper,
            request_options=request_options,
        )

    async def get_project_alt1(
        self, project_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Project, GetProjectAlt1ErrorBody]:
        """This method returns a single folder belonging to the authenticated user.

        Args:
            project_id: The ID of the folder.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/projects/{project_id}"),
            path_params=[param[float]("project_id", project_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Project],
            error_mapper=get_project_alt1_error_mapper,
            request_options=request_options,
        )

    async def get_projects(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort36OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProjectConnection, GetProjectsErrorBody]:
        """This method returns all the folders belonging to the authenticated user.

        Args:
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``date`` - Sort the results by date. * ``default``
                - Use the default sort order. * ``modified_time`` - Sort the results by last modification. * ``name`` -
                Sort the results by name. * ``pinned_on`` - Sort the results by pinned timestamp.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/projects"),
            path_params=[param[float]("user_id", user_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort36OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[ProjectConnection],
            error_mapper=get_projects_error_mapper,
            request_options=request_options,
        )

    async def get_projects_alt1(
        self,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort36OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProjectConnection, GetProjectsAlt1ErrorBody]:
        """This method returns all the folders belonging to the authenticated user.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``date`` - Sort the results by date. * ``default``
                - Use the default sort order. * ``modified_time`` - Sort the results by last modification. * ``name`` -
                Sort the results by name. * ``pinned_on`` - Sort the results by pinned timestamp.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/projects"),
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort36OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[ProjectConnection],
            error_mapper=get_projects_alt1_error_mapper,
            request_options=request_options,
        )
