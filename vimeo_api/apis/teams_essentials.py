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
    empty_response,
    json_body,
    json_decoder,
    param,
)
from ..errors.backfill_team_custom_metadata_error import (
    BackfillTeamCustomMetadataErrorBody,
    backfill_team_custom_metadata_error_mapper,
)
from ..errors.get_team_custom_metadata_incomplete_videos_error import (
    GetTeamCustomMetadataIncompleteVideosErrorBody,
    get_team_custom_metadata_incomplete_videos_error_mapper,
)
from ..errors.get_team_custom_metadata_settings_error import (
    GetTeamCustomMetadataSettingsErrorBody,
    get_team_custom_metadata_settings_error_mapper,
)
from ..errors.update_custom_metadata_field_options_error import (
    UpdateCustomMetadataFieldOptionsErrorBody,
    update_custom_metadata_field_options_error_mapper,
)
from ..errors.upsert_custom_metadata_settings_error import (
    UpsertCustomMetadataSettingsErrorBody,
    upsert_custom_metadata_settings_error_mapper,
)
from ..models.custom_metadata_settings import CustomMetadataSettings
from ..models.custom_metadata_settings_connection import CustomMetadataSettingsConnection
from ..models.enums.sort48 import Sort48OrStr
from ..models.teams_custom_metadata_backfill_request import (
    TeamsCustomMetadataBackfillRequest,
    TeamsCustomMetadataBackfillRequestDict,
)
from ..models.teams_custom_metadata_options_request import (
    TeamsCustomMetadataOptionsRequest,
    TeamsCustomMetadataOptionsRequestDict,
)
from ..models.teams_custom_metadata_request import TeamsCustomMetadataRequest, TeamsCustomMetadataRequestDict
from ..server.server import Server


class TeamsEssentials:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TeamsEssentialsWithRawResponse(client, server, auth)

    def backfill_team_custom_metadata(
        self,
        user_id: float,
        body: TeamsCustomMetadataBackfillRequest | TeamsCustomMetadataBackfillRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method applies a custom metadata value across every existing video owned by the team. Use it to populate
        a newly created field, fix a typo across a library, or align a large catalog after a workflow change.

        The backfill runs **asynchronously**. The response is returned as soon as the job is accepted, but the values
        themselves are propagated in the background and may take several minutes for large libraries. The
        ``total_videos`` count in the response is a snapshot of how many videos match the request at the moment it's
        accepted; videos uploaded after that point aren't included and need a separate backfill.

        By default, only videos that don't already have a value for the field are updated. Set ``override_existing`` to
        ``true`` to replace existing values as well.

        The value provided must match the field's data type. For example, a ``date`` field requires ``YYYY-MM-DD``, a
        ``select`` field requires one of its allowed values, and a ``multi-select`` field requires a JSON-encoded array
        of allowed values.

        Args:
            user_id: The ID of the team owner.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The backfill request was accepted. The response includes the ``field_id`` and the ``total_videos`` snapshot
            count of videos that will be updated in the background.

        Raises:
            ApiError: Error code 2204: The request is malformed, the field doesn't exist for the team, or the value
                doesn't match the field's data type. The authentication credentials are missing or invalid. The
                authenticated user doesn't have permission to manage this team's metadata. ``error`` is ``Error |
                LegacyError | RawError``."""
        return self._with_raw_response.backfill_team_custom_metadata(
            user_id, body, request_options=request_options
        ).unwrap()

    def get_team_custom_metadata_incomplete_videos(
        self,
        user_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort48OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method returns the team's videos that are missing one or more values for **mandatory** custom metadata
        fields. Use it to power dashboards that surface incomplete videos, drive curation workflows, or generate reports
        of catalog completeness.

        Each item in the response includes the video's title and identifier, a link to the video's management page, a
        thumbnail, the last modified timestamp, and the list of mandatory fields that still need a value (each with its
        ``field_id`` and ``name``).

        Only fields marked ``mandatory: true`` (see ``POST /teams/{user_id}/custom_metadata``) are considered. Teams
        with no mandatory fields receive an empty result set.

        Args:
            user_id: The ID of the team owner.
            page: The page number of the results to show. Defaults to ``1``.
            per_page: The number of items to show on each page, up to a maximum of ``100``. Defaults to ``25``.
            sort: The order in which to return the results. Defaults to ``title_asc``. Option descriptions: *
                ``modified_asc`` - Sort by last modified time, oldest first. * ``modified_desc`` - Sort by last modified
                time, newest first. * ``title_asc`` - Sort by video title, ascending. * ``title_desc`` - Sort by video
                title, descending.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The list of incomplete videos was returned. Each entry includes the video's ID, name, link, thumbnail URL,
            modified timestamp, and the list of mandatory fields that are still missing values.

        Raises:
            ApiError: Error code 2204: One of the query parameters is invalid (for example, ``per_page`` exceeds ``100``
                or ``sort`` isn't an allowed value). The authentication credentials are missing or invalid. The
                authenticated user doesn't have permission to view this team's videos. ``error`` is ``Error |
                LegacyError | RawError``."""
        return self._with_raw_response.get_team_custom_metadata_incomplete_videos(
            user_id, page=page, per_page=per_page, sort=sort, request_options=request_options
        ).unwrap()

    def get_team_custom_metadata_settings(
        self, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> CustomMetadataSettingsConnection:
        """This method returns every custom metadata field defined for the specified team.

        Custom metadata fields let teams attach structured, queryable information to videos (for example, a department
        selector, a release date, or a freeform note). Once a field is defined here, you can assign per-video values via
        ``PUT /videos/{video_id}/custom_metadata``.

        The response contains the field definitions only; per-video values are returned by the video endpoints. Use this
        method to populate a UI that lets users fill in metadata, or to discover the field IDs you need for backfills
        and value updates.

        Args:
            user_id: The ID of the team owner.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The custom metadata fields were returned.

        Raises:
            ApiError: The authentication credentials are missing or invalid. The authenticated user doesn't have
                permission to view this team's settings. Error code 5000: No such team exists. ``error`` is
                ``LegacyError | Error | RawError``."""
        return self._with_raw_response.get_team_custom_metadata_settings(
            user_id, request_options=request_options
        ).unwrap()

    def update_custom_metadata_field_options(
        self,
        user_id: float,
        body: TeamsCustomMetadataOptionsRequest | TeamsCustomMetadataOptionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CustomMetadataSettings:
        """This method modifies the allowed value list of a ``select`` or ``multi-select`` custom metadata field. Use it
        to rename an option, remove an option, or add a new option without recreating the field.

        Each entry in the ``options`` array describes one atomic change, defined by combining ``old_value`` and
        ``new_value``:

        | ``old_value`` | ``new_value`` | Operation |
        | --------------- | --------------- | ------------------------------ |
        | string | string | Rename ``old_value`` to ``new_value`` |
        | string | ``null`` / omitted | Delete ``old_value`` from the field |
        | ``null`` / omitted | string | Add ``new_value`` to the field |

        Renames are propagated to every existing video that uses the option, so the change is visible across the team's
        library. Deletes also remove the option from every video that had it set. Propagation runs in the background;
        the field's option list itself is updated synchronously and returned in the response.

        A few rules to be aware of:

        - The field must be of type ``select`` or ``multi-select``. Other types reject the request.
        - Cascading renames (renaming ``A`` to ``B``, then ``B`` to ``C`` in the same call) are not
          allowed; submit them as separate requests if you need that effect.
        - The resulting option list must not contain duplicates.

        Args:
            user_id: The ID of the team owner.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The updated field definition was returned, including its new list of allowed values.

        Raises:
            ApiError: Error code 2204: The request is malformed, the field isn't a ``select`` or ``multi-select``, the
                operations contain a cascading rename, or the resulting option list would contain duplicates. The
                authentication credentials are missing or invalid. The authenticated user doesn't have permission to
                manage this team's metadata. ``error`` is ``Error | LegacyError | RawError``."""
        return self._with_raw_response.update_custom_metadata_field_options(
            user_id, body, request_options=request_options
        ).unwrap()

    def upsert_custom_metadata_settings(
        self,
        user_id: float,
        *,
        body: TeamsCustomMetadataRequest | TeamsCustomMetadataRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[CustomMetadataSettings]:
        """This method creates, updates, or deletes custom metadata fields for a team in a single request. Each entry in
        the ``fields`` array is treated independently:

        - To **create** a new field, omit ``id`` and provide ``name``, ``type``, and ``mandatory``.
        - To **update** an existing field, provide ``id`` along with the values you want to change.
          Other values are left untouched.
        - To **delete** an existing field, provide ``id`` and set ``delete: true``. Deleting a field
          also removes every value assigned to it across the team's videos.

        Some constraints are worth knowing up front:

        - A team can have a maximum of 20 custom metadata fields. Requests that would exceed
          that limit after deletes are applied are rejected.
        - The ``type`` of an existing field can't be changed once the field is created.
        - A field that was created as optional can't be made ``mandatory`` later.
        - All operations in the request are applied as a single batch; if any one fails the
          whole request is rejected and no changes are saved.

        Args:
            user_id: The ID of the team owner.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The updated set of custom metadata fields was returned.

        Raises:
            ApiError: Error code 2204: The request is malformed, exceeds the 20-field limit, references an unknown
                field, or attempts an operation that isn't allowed (such as changing a field's ``type``). The
                authentication credentials are missing or invalid. The authenticated user doesn't have permission to
                manage this team's settings. ``error`` is ``Error | LegacyError | RawError``."""
        return self._with_raw_response.upsert_custom_metadata_settings(
            user_id, body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> TeamsEssentialsWithRawResponse:
        return self._with_raw_response


class AsyncTeamsEssentials:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTeamsEssentialsWithRawResponse(client, server, auth)

    async def backfill_team_custom_metadata(
        self,
        user_id: float,
        body: TeamsCustomMetadataBackfillRequest | TeamsCustomMetadataBackfillRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method applies a custom metadata value across every existing video owned by the team. Use it to populate
        a newly created field, fix a typo across a library, or align a large catalog after a workflow change.

        The backfill runs **asynchronously**. The response is returned as soon as the job is accepted, but the values
        themselves are propagated in the background and may take several minutes for large libraries. The
        ``total_videos`` count in the response is a snapshot of how many videos match the request at the moment it's
        accepted; videos uploaded after that point aren't included and need a separate backfill.

        By default, only videos that don't already have a value for the field are updated. Set ``override_existing`` to
        ``true`` to replace existing values as well.

        The value provided must match the field's data type. For example, a ``date`` field requires ``YYYY-MM-DD``, a
        ``select`` field requires one of its allowed values, and a ``multi-select`` field requires a JSON-encoded array
        of allowed values.

        Args:
            user_id: The ID of the team owner.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The backfill request was accepted. The response includes the ``field_id`` and the ``total_videos`` snapshot
            count of videos that will be updated in the background.

        Raises:
            ApiError: Error code 2204: The request is malformed, the field doesn't exist for the team, or the value
                doesn't match the field's data type. The authentication credentials are missing or invalid. The
                authenticated user doesn't have permission to manage this team's metadata. ``error`` is ``Error |
                LegacyError | RawError``."""
        return (
            await self._with_raw_response.backfill_team_custom_metadata(user_id, body, request_options=request_options)
        ).unwrap()

    async def get_team_custom_metadata_incomplete_videos(
        self,
        user_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort48OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method returns the team's videos that are missing one or more values for **mandatory** custom metadata
        fields. Use it to power dashboards that surface incomplete videos, drive curation workflows, or generate reports
        of catalog completeness.

        Each item in the response includes the video's title and identifier, a link to the video's management page, a
        thumbnail, the last modified timestamp, and the list of mandatory fields that still need a value (each with its
        ``field_id`` and ``name``).

        Only fields marked ``mandatory: true`` (see ``POST /teams/{user_id}/custom_metadata``) are considered. Teams
        with no mandatory fields receive an empty result set.

        Args:
            user_id: The ID of the team owner.
            page: The page number of the results to show. Defaults to ``1``.
            per_page: The number of items to show on each page, up to a maximum of ``100``. Defaults to ``25``.
            sort: The order in which to return the results. Defaults to ``title_asc``. Option descriptions: *
                ``modified_asc`` - Sort by last modified time, oldest first. * ``modified_desc`` - Sort by last modified
                time, newest first. * ``title_asc`` - Sort by video title, ascending. * ``title_desc`` - Sort by video
                title, descending.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The list of incomplete videos was returned. Each entry includes the video's ID, name, link, thumbnail URL,
            modified timestamp, and the list of mandatory fields that are still missing values.

        Raises:
            ApiError: Error code 2204: One of the query parameters is invalid (for example, ``per_page`` exceeds ``100``
                or ``sort`` isn't an allowed value). The authentication credentials are missing or invalid. The
                authenticated user doesn't have permission to view this team's videos. ``error`` is ``Error |
                LegacyError | RawError``."""
        return (
            await self._with_raw_response.get_team_custom_metadata_incomplete_videos(
                user_id, page=page, per_page=per_page, sort=sort, request_options=request_options
            )
        ).unwrap()

    async def get_team_custom_metadata_settings(
        self, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> CustomMetadataSettingsConnection:
        """This method returns every custom metadata field defined for the specified team.

        Custom metadata fields let teams attach structured, queryable information to videos (for example, a department
        selector, a release date, or a freeform note). Once a field is defined here, you can assign per-video values via
        ``PUT /videos/{video_id}/custom_metadata``.

        The response contains the field definitions only; per-video values are returned by the video endpoints. Use this
        method to populate a UI that lets users fill in metadata, or to discover the field IDs you need for backfills
        and value updates.

        Args:
            user_id: The ID of the team owner.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The custom metadata fields were returned.

        Raises:
            ApiError: The authentication credentials are missing or invalid. The authenticated user doesn't have
                permission to view this team's settings. Error code 5000: No such team exists. ``error`` is
                ``LegacyError | Error | RawError``."""
        return (
            await self._with_raw_response.get_team_custom_metadata_settings(user_id, request_options=request_options)
        ).unwrap()

    async def update_custom_metadata_field_options(
        self,
        user_id: float,
        body: TeamsCustomMetadataOptionsRequest | TeamsCustomMetadataOptionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CustomMetadataSettings:
        """This method modifies the allowed value list of a ``select`` or ``multi-select`` custom metadata field. Use it
        to rename an option, remove an option, or add a new option without recreating the field.

        Each entry in the ``options`` array describes one atomic change, defined by combining ``old_value`` and
        ``new_value``:

        | ``old_value`` | ``new_value`` | Operation |
        | --------------- | --------------- | ------------------------------ |
        | string | string | Rename ``old_value`` to ``new_value`` |
        | string | ``null`` / omitted | Delete ``old_value`` from the field |
        | ``null`` / omitted | string | Add ``new_value`` to the field |

        Renames are propagated to every existing video that uses the option, so the change is visible across the team's
        library. Deletes also remove the option from every video that had it set. Propagation runs in the background;
        the field's option list itself is updated synchronously and returned in the response.

        A few rules to be aware of:

        - The field must be of type ``select`` or ``multi-select``. Other types reject the request.
        - Cascading renames (renaming ``A`` to ``B``, then ``B`` to ``C`` in the same call) are not
          allowed; submit them as separate requests if you need that effect.
        - The resulting option list must not contain duplicates.

        Args:
            user_id: The ID of the team owner.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The updated field definition was returned, including its new list of allowed values.

        Raises:
            ApiError: Error code 2204: The request is malformed, the field isn't a ``select`` or ``multi-select``, the
                operations contain a cascading rename, or the resulting option list would contain duplicates. The
                authentication credentials are missing or invalid. The authenticated user doesn't have permission to
                manage this team's metadata. ``error`` is ``Error | LegacyError | RawError``."""
        return (
            await self._with_raw_response.update_custom_metadata_field_options(
                user_id, body, request_options=request_options
            )
        ).unwrap()

    async def upsert_custom_metadata_settings(
        self,
        user_id: float,
        *,
        body: TeamsCustomMetadataRequest | TeamsCustomMetadataRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[CustomMetadataSettings]:
        """This method creates, updates, or deletes custom metadata fields for a team in a single request. Each entry in
        the ``fields`` array is treated independently:

        - To **create** a new field, omit ``id`` and provide ``name``, ``type``, and ``mandatory``.
        - To **update** an existing field, provide ``id`` along with the values you want to change.
          Other values are left untouched.
        - To **delete** an existing field, provide ``id`` and set ``delete: true``. Deleting a field
          also removes every value assigned to it across the team's videos.

        Some constraints are worth knowing up front:

        - A team can have a maximum of 20 custom metadata fields. Requests that would exceed
          that limit after deletes are applied are rejected.
        - The ``type`` of an existing field can't be changed once the field is created.
        - A field that was created as optional can't be made ``mandatory`` later.
        - All operations in the request are applied as a single batch; if any one fails the
          whole request is rejected and no changes are saved.

        Args:
            user_id: The ID of the team owner.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The updated set of custom metadata fields was returned.

        Raises:
            ApiError: Error code 2204: The request is malformed, exceeds the 20-field limit, references an unknown
                field, or attempts an operation that isn't allowed (such as changing a field's ``type``). The
                authentication credentials are missing or invalid. The authenticated user doesn't have permission to
                manage this team's settings. ``error`` is ``Error | LegacyError | RawError``."""
        return (
            await self._with_raw_response.upsert_custom_metadata_settings(
                user_id, body=body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncTeamsEssentialsWithRawResponse:
        return self._with_raw_response


class TeamsEssentialsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def backfill_team_custom_metadata(
        self,
        user_id: float,
        body: TeamsCustomMetadataBackfillRequest | TeamsCustomMetadataBackfillRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, BackfillTeamCustomMetadataErrorBody]:
        """This method applies a custom metadata value across every existing video owned by the team. Use it to populate
        a newly created field, fix a typo across a library, or align a large catalog after a workflow change.

        The backfill runs **asynchronously**. The response is returned as soon as the job is accepted, but the values
        themselves are propagated in the background and may take several minutes for large libraries. The
        ``total_videos`` count in the response is a snapshot of how many videos match the request at the moment it's
        accepted; videos uploaded after that point aren't included and need a separate backfill.

        By default, only videos that don't already have a value for the field are updated. Set ``override_existing`` to
        ``true`` to replace existing values as well.

        The value provided must match the field's data type. For example, a ``date`` field requires ``YYYY-MM-DD``, a
        ``select`` field requires one of its allowed values, and a ``multi-select`` field requires a JSON-encoded array
        of allowed values.

        Args:
            user_id: The ID of the team owner.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/teams/{user_id}/custom_metadata/backfill"),
            path_params=[param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TeamsCustomMetadataBackfillRequest | TeamsCustomMetadataBackfillRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=backfill_team_custom_metadata_error_mapper,
            request_options=request_options,
        )

    def get_team_custom_metadata_incomplete_videos(
        self,
        user_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort48OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, GetTeamCustomMetadataIncompleteVideosErrorBody]:
        """This method returns the team's videos that are missing one or more values for **mandatory** custom metadata
        fields. Use it to power dashboards that surface incomplete videos, drive curation workflows, or generate reports
        of catalog completeness.

        Each item in the response includes the video's title and identifier, a link to the video's management page, a
        thumbnail, the last modified timestamp, and the list of mandatory fields that still need a value (each with its
        ``field_id`` and ``name``).

        Only fields marked ``mandatory: true`` (see ``POST /teams/{user_id}/custom_metadata``) are considered. Teams
        with no mandatory fields receive an empty result set.

        Args:
            user_id: The ID of the team owner.
            page: The page number of the results to show. Defaults to ``1``.
            per_page: The number of items to show on each page, up to a maximum of ``100``. Defaults to ``25``.
            sort: The order in which to return the results. Defaults to ``title_asc``. Option descriptions: *
                ``modified_asc`` - Sort by last modified time, oldest first. * ``modified_desc`` - Sort by last modified
                time, newest first. * ``title_asc`` - Sort by video title, ascending. * ``title_desc`` - Sort by video
                title, descending.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/teams/{user_id}/custom_metadata/incomplete_videos"),
            path_params=[param[float]("user_id", user_id)],
            query_params=[
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[Sort48OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=get_team_custom_metadata_incomplete_videos_error_mapper,
            request_options=request_options,
        )

    def get_team_custom_metadata_settings(
        self, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CustomMetadataSettingsConnection, GetTeamCustomMetadataSettingsErrorBody]:
        """This method returns every custom metadata field defined for the specified team.

        Custom metadata fields let teams attach structured, queryable information to videos (for example, a department
        selector, a release date, or a freeform note). Once a field is defined here, you can assign per-video values via
        ``PUT /videos/{video_id}/custom_metadata``.

        The response contains the field definitions only; per-video values are returned by the video endpoints. Use this
        method to populate a UI that lets users fill in metadata, or to discover the field IDs you need for backfills
        and value updates.

        Args:
            user_id: The ID of the team owner.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/teams/{user_id}/custom_metadata"),
            path_params=[param[float]("user_id", user_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[CustomMetadataSettingsConnection],
            error_mapper=get_team_custom_metadata_settings_error_mapper,
            request_options=request_options,
        )

    def update_custom_metadata_field_options(
        self,
        user_id: float,
        body: TeamsCustomMetadataOptionsRequest | TeamsCustomMetadataOptionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CustomMetadataSettings, UpdateCustomMetadataFieldOptionsErrorBody]:
        """This method modifies the allowed value list of a ``select`` or ``multi-select`` custom metadata field. Use it
        to rename an option, remove an option, or add a new option without recreating the field.

        Each entry in the ``options`` array describes one atomic change, defined by combining ``old_value`` and
        ``new_value``:

        | ``old_value`` | ``new_value`` | Operation |
        | --------------- | --------------- | ------------------------------ |
        | string | string | Rename ``old_value`` to ``new_value`` |
        | string | ``null`` / omitted | Delete ``old_value`` from the field |
        | ``null`` / omitted | string | Add ``new_value`` to the field |

        Renames are propagated to every existing video that uses the option, so the change is visible across the team's
        library. Deletes also remove the option from every video that had it set. Propagation runs in the background;
        the field's option list itself is updated synchronously and returned in the response.

        A few rules to be aware of:

        - The field must be of type ``select`` or ``multi-select``. Other types reject the request.
        - Cascading renames (renaming ``A`` to ``B``, then ``B`` to ``C`` in the same call) are not
          allowed; submit them as separate requests if you need that effect.
        - The resulting option list must not contain duplicates.

        Args:
            user_id: The ID of the team owner.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/teams/{user_id}/custom_metadata/options"),
            path_params=[param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TeamsCustomMetadataOptionsRequest | TeamsCustomMetadataOptionsRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[CustomMetadataSettings],
            error_mapper=update_custom_metadata_field_options_error_mapper,
            request_options=request_options,
        )

    def upsert_custom_metadata_settings(
        self,
        user_id: float,
        *,
        body: TeamsCustomMetadataRequest | TeamsCustomMetadataRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[CustomMetadataSettings], UpsertCustomMetadataSettingsErrorBody]:
        """This method creates, updates, or deletes custom metadata fields for a team in a single request. Each entry in
        the ``fields`` array is treated independently:

        - To **create** a new field, omit ``id`` and provide ``name``, ``type``, and ``mandatory``.
        - To **update** an existing field, provide ``id`` along with the values you want to change.
          Other values are left untouched.
        - To **delete** an existing field, provide ``id`` and set ``delete: true``. Deleting a field
          also removes every value assigned to it across the team's videos.

        Some constraints are worth knowing up front:

        - A team can have a maximum of 20 custom metadata fields. Requests that would exceed
          that limit after deletes are applied are rejected.
        - The ``type`` of an existing field can't be changed once the field is created.
        - A field that was created as optional can't be made ``mandatory`` later.
        - All operations in the request are applied as a single batch; if any one fails the
          whole request is rejected and no changes are saved.

        Args:
            user_id: The ID of the team owner.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/teams/{user_id}/custom_metadata"),
            path_params=[param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TeamsCustomMetadataRequest | TeamsCustomMetadataRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[list[CustomMetadataSettings]],
            error_mapper=upsert_custom_metadata_settings_error_mapper,
            request_options=request_options,
        )


class AsyncTeamsEssentialsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def backfill_team_custom_metadata(
        self,
        user_id: float,
        body: TeamsCustomMetadataBackfillRequest | TeamsCustomMetadataBackfillRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, BackfillTeamCustomMetadataErrorBody]:
        """This method applies a custom metadata value across every existing video owned by the team. Use it to populate
        a newly created field, fix a typo across a library, or align a large catalog after a workflow change.

        The backfill runs **asynchronously**. The response is returned as soon as the job is accepted, but the values
        themselves are propagated in the background and may take several minutes for large libraries. The
        ``total_videos`` count in the response is a snapshot of how many videos match the request at the moment it's
        accepted; videos uploaded after that point aren't included and need a separate backfill.

        By default, only videos that don't already have a value for the field are updated. Set ``override_existing`` to
        ``true`` to replace existing values as well.

        The value provided must match the field's data type. For example, a ``date`` field requires ``YYYY-MM-DD``, a
        ``select`` field requires one of its allowed values, and a ``multi-select`` field requires a JSON-encoded array
        of allowed values.

        Args:
            user_id: The ID of the team owner.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/teams/{user_id}/custom_metadata/backfill"),
            path_params=[param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TeamsCustomMetadataBackfillRequest | TeamsCustomMetadataBackfillRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=backfill_team_custom_metadata_error_mapper,
            request_options=request_options,
        )

    async def get_team_custom_metadata_incomplete_videos(
        self,
        user_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort48OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, GetTeamCustomMetadataIncompleteVideosErrorBody]:
        """This method returns the team's videos that are missing one or more values for **mandatory** custom metadata
        fields. Use it to power dashboards that surface incomplete videos, drive curation workflows, or generate reports
        of catalog completeness.

        Each item in the response includes the video's title and identifier, a link to the video's management page, a
        thumbnail, the last modified timestamp, and the list of mandatory fields that still need a value (each with its
        ``field_id`` and ``name``).

        Only fields marked ``mandatory: true`` (see ``POST /teams/{user_id}/custom_metadata``) are considered. Teams
        with no mandatory fields receive an empty result set.

        Args:
            user_id: The ID of the team owner.
            page: The page number of the results to show. Defaults to ``1``.
            per_page: The number of items to show on each page, up to a maximum of ``100``. Defaults to ``25``.
            sort: The order in which to return the results. Defaults to ``title_asc``. Option descriptions: *
                ``modified_asc`` - Sort by last modified time, oldest first. * ``modified_desc`` - Sort by last modified
                time, newest first. * ``title_asc`` - Sort by video title, ascending. * ``title_desc`` - Sort by video
                title, descending.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/teams/{user_id}/custom_metadata/incomplete_videos"),
            path_params=[param[float]("user_id", user_id)],
            query_params=[
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[Sort48OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=get_team_custom_metadata_incomplete_videos_error_mapper,
            request_options=request_options,
        )

    async def get_team_custom_metadata_settings(
        self, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CustomMetadataSettingsConnection, GetTeamCustomMetadataSettingsErrorBody]:
        """This method returns every custom metadata field defined for the specified team.

        Custom metadata fields let teams attach structured, queryable information to videos (for example, a department
        selector, a release date, or a freeform note). Once a field is defined here, you can assign per-video values via
        ``PUT /videos/{video_id}/custom_metadata``.

        The response contains the field definitions only; per-video values are returned by the video endpoints. Use this
        method to populate a UI that lets users fill in metadata, or to discover the field IDs you need for backfills
        and value updates.

        Args:
            user_id: The ID of the team owner.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/teams/{user_id}/custom_metadata"),
            path_params=[param[float]("user_id", user_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[CustomMetadataSettingsConnection],
            error_mapper=get_team_custom_metadata_settings_error_mapper,
            request_options=request_options,
        )

    async def update_custom_metadata_field_options(
        self,
        user_id: float,
        body: TeamsCustomMetadataOptionsRequest | TeamsCustomMetadataOptionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CustomMetadataSettings, UpdateCustomMetadataFieldOptionsErrorBody]:
        """This method modifies the allowed value list of a ``select`` or ``multi-select`` custom metadata field. Use it
        to rename an option, remove an option, or add a new option without recreating the field.

        Each entry in the ``options`` array describes one atomic change, defined by combining ``old_value`` and
        ``new_value``:

        | ``old_value`` | ``new_value`` | Operation |
        | --------------- | --------------- | ------------------------------ |
        | string | string | Rename ``old_value`` to ``new_value`` |
        | string | ``null`` / omitted | Delete ``old_value`` from the field |
        | ``null`` / omitted | string | Add ``new_value`` to the field |

        Renames are propagated to every existing video that uses the option, so the change is visible across the team's
        library. Deletes also remove the option from every video that had it set. Propagation runs in the background;
        the field's option list itself is updated synchronously and returned in the response.

        A few rules to be aware of:

        - The field must be of type ``select`` or ``multi-select``. Other types reject the request.
        - Cascading renames (renaming ``A`` to ``B``, then ``B`` to ``C`` in the same call) are not
          allowed; submit them as separate requests if you need that effect.
        - The resulting option list must not contain duplicates.

        Args:
            user_id: The ID of the team owner.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/teams/{user_id}/custom_metadata/options"),
            path_params=[param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TeamsCustomMetadataOptionsRequest | TeamsCustomMetadataOptionsRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[CustomMetadataSettings],
            error_mapper=update_custom_metadata_field_options_error_mapper,
            request_options=request_options,
        )

    async def upsert_custom_metadata_settings(
        self,
        user_id: float,
        *,
        body: TeamsCustomMetadataRequest | TeamsCustomMetadataRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[CustomMetadataSettings], UpsertCustomMetadataSettingsErrorBody]:
        """This method creates, updates, or deletes custom metadata fields for a team in a single request. Each entry in
        the ``fields`` array is treated independently:

        - To **create** a new field, omit ``id`` and provide ``name``, ``type``, and ``mandatory``.
        - To **update** an existing field, provide ``id`` along with the values you want to change.
          Other values are left untouched.
        - To **delete** an existing field, provide ``id`` and set ``delete: true``. Deleting a field
          also removes every value assigned to it across the team's videos.

        Some constraints are worth knowing up front:

        - A team can have a maximum of 20 custom metadata fields. Requests that would exceed
          that limit after deletes are applied are rejected.
        - The ``type`` of an existing field can't be changed once the field is created.
        - A field that was created as optional can't be made ``mandatory`` later.
        - All operations in the request are applied as a single batch; if any one fails the
          whole request is rejected and no changes are saved.

        Args:
            user_id: The ID of the team owner.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/teams/{user_id}/custom_metadata"),
            path_params=[param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TeamsCustomMetadataRequest | TeamsCustomMetadataRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[list[CustomMetadataSettings]],
            error_mapper=upsert_custom_metadata_settings_error_mapper,
            request_options=request_options,
        )
