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
from ..errors.create_live_event_thumbnail_alt1_error import (
    CreateLiveEventThumbnailAlt1ErrorBody,
    create_live_event_thumbnail_alt1_error_mapper,
)
from ..errors.create_live_event_thumbnail_alt2_error import (
    CreateLiveEventThumbnailAlt2ErrorBody,
    create_live_event_thumbnail_alt2_error_mapper,
)
from ..errors.create_live_event_thumbnail_error import (
    CreateLiveEventThumbnailErrorBody,
    create_live_event_thumbnail_error_mapper,
)
from ..errors.delete_live_event_thumbnail_alt1_error import (
    DeleteLiveEventThumbnailAlt1ErrorBody,
    delete_live_event_thumbnail_alt1_error_mapper,
)
from ..errors.delete_live_event_thumbnail_alt2_error import (
    DeleteLiveEventThumbnailAlt2ErrorBody,
    delete_live_event_thumbnail_alt2_error_mapper,
)
from ..errors.delete_live_event_thumbnail_error import (
    DeleteLiveEventThumbnailErrorBody,
    delete_live_event_thumbnail_error_mapper,
)
from ..errors.edit_live_event_thumbnail_alt1_error import (
    EditLiveEventThumbnailAlt1ErrorBody,
    edit_live_event_thumbnail_alt1_error_mapper,
)
from ..errors.edit_live_event_thumbnail_alt2_error import (
    EditLiveEventThumbnailAlt2ErrorBody,
    edit_live_event_thumbnail_alt2_error_mapper,
)
from ..errors.edit_live_event_thumbnail_error import (
    EditLiveEventThumbnailErrorBody,
    edit_live_event_thumbnail_error_mapper,
)
from ..errors.get_live_event_thumbnail_alt1_error import (
    GetLiveEventThumbnailAlt1ErrorBody,
    get_live_event_thumbnail_alt1_error_mapper,
)
from ..errors.get_live_event_thumbnail_alt2_error import (
    GetLiveEventThumbnailAlt2ErrorBody,
    get_live_event_thumbnail_alt2_error_mapper,
)
from ..errors.get_live_event_thumbnail_error import (
    GetLiveEventThumbnailErrorBody,
    get_live_event_thumbnail_error_mapper,
)
from ..errors.get_live_event_thumbnails_alt1_error import (
    GetLiveEventThumbnailsAlt1ErrorBody,
    get_live_event_thumbnails_alt1_error_mapper,
)
from ..errors.get_live_event_thumbnails_alt2_error import (
    GetLiveEventThumbnailsAlt2ErrorBody,
    get_live_event_thumbnails_alt2_error_mapper,
)
from ..errors.get_live_event_thumbnails_error import (
    GetLiveEventThumbnailsErrorBody,
    get_live_event_thumbnails_error_mapper,
)
from ..models.live_events_pictures_request import LiveEventsPicturesRequest, LiveEventsPicturesRequestDict
from ..models.me_live_events_pictures_request import MeLiveEventsPicturesRequest, MeLiveEventsPicturesRequestDict
from ..models.picture import Picture
from ..models.picture_connection import PictureConnection
from ..models.users_live_events_pictures_request import (
    UsersLiveEventsPicturesRequest,
    UsersLiveEventsPicturesRequestDict,
)
from ..models.users_live_events_pictures_thumbnail_id_request import (
    UsersLiveEventsPicturesThumbnailIdRequest,
    UsersLiveEventsPicturesThumbnailIdRequestDict,
)
from ..server.server import Server


class LiveEventThumbnails:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = LiveEventThumbnailsWithRawResponse(client, server, auth)

    def create_live_event_thumbnail(
        self,
        live_event_id: float,
        user_id: float,
        *,
        body: UsersLiveEventsPicturesRequest | UsersLiveEventsPicturesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Picture:
        """This method creates a thumbnail image for the specified event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The thumbnail was created.

        Raises:
            ApiError: * Error code 3200: The authenticated user can't delete the thumbnails for the event. * Error code
                3422: The authenticated user can't create a thumbnail for the event. Error code 5000: No such event or
                user exists. ``error`` is ``Error | RawError``."""
        return unwrap(
            self._with_raw_response.create_live_event_thumbnail(
                live_event_id, user_id, body=body, request_options=request_options
            ),
        )

    def create_live_event_thumbnail_alt1(
        self,
        live_event_id: float,
        *,
        body: LiveEventsPicturesRequest | LiveEventsPicturesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Picture:
        """This method creates a thumbnail image for the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The thumbnail was created.

        Raises:
            ApiError: * Error code 3200: The authenticated user can't delete the thumbnails for the event. * Error code
                3422: The authenticated user can't create a thumbnail for the event. Error code 5000: No such event or
                user exists. ``error`` is ``Error | RawError``."""
        return unwrap(
            self._with_raw_response.create_live_event_thumbnail_alt1(
                live_event_id, body=body, request_options=request_options
            ),
        )

    def create_live_event_thumbnail_alt2(
        self,
        live_event_id: float,
        *,
        body: MeLiveEventsPicturesRequest | MeLiveEventsPicturesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Picture:
        """This method creates a thumbnail image for the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The thumbnail was created.

        Raises:
            ApiError: * Error code 3200: The authenticated user can't delete the thumbnails for the event. * Error code
                3422: The authenticated user can't create a thumbnail for the event. Error code 5000: No such event or
                user exists. ``error`` is ``Error | RawError``."""
        return unwrap(
            self._with_raw_response.create_live_event_thumbnail_alt2(
                live_event_id, body=body, request_options=request_options
            ),
        )

    def delete_live_event_thumbnail(
        self,
        live_event_id: float,
        thumbnail_id: float,
        user_id: float,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method deletes a thumbnail image for the specified event.

        Args:
            live_event_id: The ID of the event.
            thumbnail_id: The ID of the thumbnail.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The thumbnail was deleted.

        Raises:
            ApiError: * Error code 3200: The authenticated user can't delete the thumbnail for the event. * Error code
                3422: The authenticated user can't delete the thumbnail. Error code 5000: No such event, thumbnail, or
                user exists. ``error`` is ``Error | RawError``."""
        return unwrap(
            self._with_raw_response.delete_live_event_thumbnail(
                live_event_id, thumbnail_id, user_id, request_options=request_options
            ),
        )

    def delete_live_event_thumbnail_alt1(
        self, live_event_id: float, thumbnail_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes a thumbnail image for the specified event.

        Args:
            live_event_id: The ID of the event.
            thumbnail_id: The ID of the thumbnail.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The thumbnail was deleted.

        Raises:
            ApiError: * Error code 3200: The authenticated user can't delete the thumbnail for the event. * Error code
                3422: The authenticated user can't delete the thumbnail. Error code 5000: No such event, thumbnail, or
                user exists. ``error`` is ``Error | RawError``."""
        return unwrap(
            self._with_raw_response.delete_live_event_thumbnail_alt1(
                live_event_id, thumbnail_id, request_options=request_options
            ),
        )

    def delete_live_event_thumbnail_alt2(
        self, live_event_id: float, thumbnail_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes a thumbnail image for the specified event.

        Args:
            live_event_id: The ID of the event.
            thumbnail_id: The ID of the thumbnail.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The thumbnail was deleted.

        Raises:
            ApiError: * Error code 3200: The authenticated user can't delete the thumbnail for the event. * Error code
                3422: The authenticated user can't delete the thumbnail. Error code 5000: No such event, thumbnail, or
                user exists. ``error`` is ``Error | RawError``."""
        return unwrap(
            self._with_raw_response.delete_live_event_thumbnail_alt2(
                live_event_id, thumbnail_id, request_options=request_options
            ),
        )

    def edit_live_event_thumbnail(
        self,
        live_event_id: float,
        thumbnail_id: float,
        user_id: float,
        *,
        body: UsersLiveEventsPicturesThumbnailIdRequest | UsersLiveEventsPicturesThumbnailIdRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Picture:
        """This method edits a thumbnail image for the specified event.

        Args:
            live_event_id: The ID of the event.
            thumbnail_id: The ID of the thumbnail.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The thumbnail was edited.

        Raises:
            ApiError: * Error code 3200: The authenticated user can't update the thumbnail for the event. * Error code
                3422: The authenticated user can't edit the thumbnail of the event. Error code 5000: No such event,
                thumbnail, or user exists. ``error`` is ``Error | RawError``."""
        return unwrap(
            self._with_raw_response.edit_live_event_thumbnail(
                live_event_id, thumbnail_id, user_id, body=body, request_options=request_options
            ),
        )

    def edit_live_event_thumbnail_alt1(
        self,
        live_event_id: float,
        thumbnail_id: float,
        *,
        body: LiveEventsPicturesRequest | LiveEventsPicturesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Picture:
        """This method edits a thumbnail image for the specified event.

        Args:
            live_event_id: The ID of the event.
            thumbnail_id: The ID of the thumbnail.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The thumbnail was edited.

        Raises:
            ApiError: * Error code 3200: The authenticated user can't update the thumbnail for the event. * Error code
                3422: The authenticated user can't edit the thumbnail of the event. Error code 5000: No such event,
                thumbnail, or user exists. ``error`` is ``Error | RawError``."""
        return unwrap(
            self._with_raw_response.edit_live_event_thumbnail_alt1(
                live_event_id, thumbnail_id, body=body, request_options=request_options
            ),
        )

    def edit_live_event_thumbnail_alt2(
        self,
        live_event_id: float,
        thumbnail_id: float,
        *,
        body: MeLiveEventsPicturesRequest | MeLiveEventsPicturesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Picture:
        """This method edits a thumbnail image for the specified event.

        Args:
            live_event_id: The ID of the event.
            thumbnail_id: The ID of the thumbnail.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The thumbnail was edited.

        Raises:
            ApiError: * Error code 3200: The authenticated user can't update the thumbnail for the event. * Error code
                3422: The authenticated user can't edit the thumbnail of the event. Error code 5000: No such event,
                thumbnail, or user exists. ``error`` is ``Error | RawError``."""
        return unwrap(
            self._with_raw_response.edit_live_event_thumbnail_alt2(
                live_event_id, thumbnail_id, body=body, request_options=request_options
            ),
        )

    def get_live_event_thumbnail(
        self,
        live_event_id: float,
        thumbnail_id: float,
        user_id: float,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Picture:
        """This method returns a single thumbnail image of the specified event.

        Args:
            live_event_id: The ID of the event.
            thumbnail_id: The ID of the thumbnail.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The thumbnail was returned.

        Raises:
            ApiError: Error code 3200: The authenticated user can't access the thumbnail. Error code 5000: No such
                event, thumbnail, or user exists. ``error`` is ``Error | RawError``."""
        return unwrap(
            self._with_raw_response.get_live_event_thumbnail(
                live_event_id, thumbnail_id, user_id, request_options=request_options
            ),
        )

    def get_live_event_thumbnail_alt1(
        self, live_event_id: float, thumbnail_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Picture:
        """This method returns a single thumbnail image of the specified event.

        Args:
            live_event_id: The ID of the event.
            thumbnail_id: The ID of the thumbnail.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The thumbnail was returned.

        Raises:
            ApiError: Error code 3200: The authenticated user can't access the thumbnail. Error code 5000: No such
                event, thumbnail, or user exists. ``error`` is ``Error | RawError``."""
        return unwrap(
            self._with_raw_response.get_live_event_thumbnail_alt1(
                live_event_id, thumbnail_id, request_options=request_options
            ),
        )

    def get_live_event_thumbnail_alt2(
        self, live_event_id: float, thumbnail_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Picture:
        """This method returns a single thumbnail image of the specified event.

        Args:
            live_event_id: The ID of the event.
            thumbnail_id: The ID of the thumbnail.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The thumbnail was returned.

        Raises:
            ApiError: Error code 3200: The authenticated user can't access the thumbnail. Error code 5000: No such
                event, thumbnail, or user exists. ``error`` is ``Error | RawError``."""
        return unwrap(
            self._with_raw_response.get_live_event_thumbnail_alt2(
                live_event_id, thumbnail_id, request_options=request_options
            ),
        )

    def get_live_event_thumbnails(
        self, live_event_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> PictureConnection:
        """This method returns every thumbnail image of the specified event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The thumbnails were returned.

        Raises:
            ApiError: Error code 5000: No such event or user exists. ``error`` is ``Error | RawError``."""
        return unwrap(
            self._with_raw_response.get_live_event_thumbnails(live_event_id, user_id, request_options=request_options)
        )

    def get_live_event_thumbnails_alt1(
        self, live_event_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> PictureConnection:
        """This method returns every thumbnail image of the specified event.

        Args:
            live_event_id: The ID of the event.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The thumbnails were returned.

        Raises:
            ApiError: Error code 5000: No such event or user exists. ``error`` is ``Error | RawError``."""
        return unwrap(
            self._with_raw_response.get_live_event_thumbnails_alt1(live_event_id, request_options=request_options)
        )

    def get_live_event_thumbnails_alt2(
        self, live_event_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> PictureConnection:
        """This method returns every thumbnail image of the specified event.

        Args:
            live_event_id: The ID of the event.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The thumbnails were returned.

        Raises:
            ApiError: Error code 5000: No such event or user exists. ``error`` is ``Error | RawError``."""
        return unwrap(
            self._with_raw_response.get_live_event_thumbnails_alt2(live_event_id, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> LiveEventThumbnailsWithRawResponse:
        return self._with_raw_response


class AsyncLiveEventThumbnails:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncLiveEventThumbnailsWithRawResponse(client, server, auth)

    async def create_live_event_thumbnail(
        self,
        live_event_id: float,
        user_id: float,
        *,
        body: UsersLiveEventsPicturesRequest | UsersLiveEventsPicturesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Picture:
        """This method creates a thumbnail image for the specified event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The thumbnail was created.

        Raises:
            ApiError: * Error code 3200: The authenticated user can't delete the thumbnails for the event. * Error code
                3422: The authenticated user can't create a thumbnail for the event. Error code 5000: No such event or
                user exists. ``error`` is ``Error | RawError``."""
        return unwrap(
            await self._with_raw_response.create_live_event_thumbnail(
                live_event_id, user_id, body=body, request_options=request_options
            ),
        )

    async def create_live_event_thumbnail_alt1(
        self,
        live_event_id: float,
        *,
        body: LiveEventsPicturesRequest | LiveEventsPicturesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Picture:
        """This method creates a thumbnail image for the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The thumbnail was created.

        Raises:
            ApiError: * Error code 3200: The authenticated user can't delete the thumbnails for the event. * Error code
                3422: The authenticated user can't create a thumbnail for the event. Error code 5000: No such event or
                user exists. ``error`` is ``Error | RawError``."""
        return unwrap(
            await self._with_raw_response.create_live_event_thumbnail_alt1(
                live_event_id, body=body, request_options=request_options
            ),
        )

    async def create_live_event_thumbnail_alt2(
        self,
        live_event_id: float,
        *,
        body: MeLiveEventsPicturesRequest | MeLiveEventsPicturesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Picture:
        """This method creates a thumbnail image for the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The thumbnail was created.

        Raises:
            ApiError: * Error code 3200: The authenticated user can't delete the thumbnails for the event. * Error code
                3422: The authenticated user can't create a thumbnail for the event. Error code 5000: No such event or
                user exists. ``error`` is ``Error | RawError``."""
        return unwrap(
            await self._with_raw_response.create_live_event_thumbnail_alt2(
                live_event_id, body=body, request_options=request_options
            ),
        )

    async def delete_live_event_thumbnail(
        self,
        live_event_id: float,
        thumbnail_id: float,
        user_id: float,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method deletes a thumbnail image for the specified event.

        Args:
            live_event_id: The ID of the event.
            thumbnail_id: The ID of the thumbnail.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The thumbnail was deleted.

        Raises:
            ApiError: * Error code 3200: The authenticated user can't delete the thumbnail for the event. * Error code
                3422: The authenticated user can't delete the thumbnail. Error code 5000: No such event, thumbnail, or
                user exists. ``error`` is ``Error | RawError``."""
        return unwrap(
            await self._with_raw_response.delete_live_event_thumbnail(
                live_event_id, thumbnail_id, user_id, request_options=request_options
            ),
        )

    async def delete_live_event_thumbnail_alt1(
        self, live_event_id: float, thumbnail_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes a thumbnail image for the specified event.

        Args:
            live_event_id: The ID of the event.
            thumbnail_id: The ID of the thumbnail.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The thumbnail was deleted.

        Raises:
            ApiError: * Error code 3200: The authenticated user can't delete the thumbnail for the event. * Error code
                3422: The authenticated user can't delete the thumbnail. Error code 5000: No such event, thumbnail, or
                user exists. ``error`` is ``Error | RawError``."""
        return unwrap(
            await self._with_raw_response.delete_live_event_thumbnail_alt1(
                live_event_id, thumbnail_id, request_options=request_options
            ),
        )

    async def delete_live_event_thumbnail_alt2(
        self, live_event_id: float, thumbnail_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes a thumbnail image for the specified event.

        Args:
            live_event_id: The ID of the event.
            thumbnail_id: The ID of the thumbnail.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The thumbnail was deleted.

        Raises:
            ApiError: * Error code 3200: The authenticated user can't delete the thumbnail for the event. * Error code
                3422: The authenticated user can't delete the thumbnail. Error code 5000: No such event, thumbnail, or
                user exists. ``error`` is ``Error | RawError``."""
        return unwrap(
            await self._with_raw_response.delete_live_event_thumbnail_alt2(
                live_event_id, thumbnail_id, request_options=request_options
            ),
        )

    async def edit_live_event_thumbnail(
        self,
        live_event_id: float,
        thumbnail_id: float,
        user_id: float,
        *,
        body: UsersLiveEventsPicturesThumbnailIdRequest | UsersLiveEventsPicturesThumbnailIdRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Picture:
        """This method edits a thumbnail image for the specified event.

        Args:
            live_event_id: The ID of the event.
            thumbnail_id: The ID of the thumbnail.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The thumbnail was edited.

        Raises:
            ApiError: * Error code 3200: The authenticated user can't update the thumbnail for the event. * Error code
                3422: The authenticated user can't edit the thumbnail of the event. Error code 5000: No such event,
                thumbnail, or user exists. ``error`` is ``Error | RawError``."""
        return unwrap(
            await self._with_raw_response.edit_live_event_thumbnail(
                live_event_id, thumbnail_id, user_id, body=body, request_options=request_options
            ),
        )

    async def edit_live_event_thumbnail_alt1(
        self,
        live_event_id: float,
        thumbnail_id: float,
        *,
        body: LiveEventsPicturesRequest | LiveEventsPicturesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Picture:
        """This method edits a thumbnail image for the specified event.

        Args:
            live_event_id: The ID of the event.
            thumbnail_id: The ID of the thumbnail.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The thumbnail was edited.

        Raises:
            ApiError: * Error code 3200: The authenticated user can't update the thumbnail for the event. * Error code
                3422: The authenticated user can't edit the thumbnail of the event. Error code 5000: No such event,
                thumbnail, or user exists. ``error`` is ``Error | RawError``."""
        return unwrap(
            await self._with_raw_response.edit_live_event_thumbnail_alt1(
                live_event_id, thumbnail_id, body=body, request_options=request_options
            ),
        )

    async def edit_live_event_thumbnail_alt2(
        self,
        live_event_id: float,
        thumbnail_id: float,
        *,
        body: MeLiveEventsPicturesRequest | MeLiveEventsPicturesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Picture:
        """This method edits a thumbnail image for the specified event.

        Args:
            live_event_id: The ID of the event.
            thumbnail_id: The ID of the thumbnail.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The thumbnail was edited.

        Raises:
            ApiError: * Error code 3200: The authenticated user can't update the thumbnail for the event. * Error code
                3422: The authenticated user can't edit the thumbnail of the event. Error code 5000: No such event,
                thumbnail, or user exists. ``error`` is ``Error | RawError``."""
        return unwrap(
            await self._with_raw_response.edit_live_event_thumbnail_alt2(
                live_event_id, thumbnail_id, body=body, request_options=request_options
            ),
        )

    async def get_live_event_thumbnail(
        self,
        live_event_id: float,
        thumbnail_id: float,
        user_id: float,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Picture:
        """This method returns a single thumbnail image of the specified event.

        Args:
            live_event_id: The ID of the event.
            thumbnail_id: The ID of the thumbnail.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The thumbnail was returned.

        Raises:
            ApiError: Error code 3200: The authenticated user can't access the thumbnail. Error code 5000: No such
                event, thumbnail, or user exists. ``error`` is ``Error | RawError``."""
        return unwrap(
            await self._with_raw_response.get_live_event_thumbnail(
                live_event_id, thumbnail_id, user_id, request_options=request_options
            ),
        )

    async def get_live_event_thumbnail_alt1(
        self, live_event_id: float, thumbnail_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Picture:
        """This method returns a single thumbnail image of the specified event.

        Args:
            live_event_id: The ID of the event.
            thumbnail_id: The ID of the thumbnail.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The thumbnail was returned.

        Raises:
            ApiError: Error code 3200: The authenticated user can't access the thumbnail. Error code 5000: No such
                event, thumbnail, or user exists. ``error`` is ``Error | RawError``."""
        return unwrap(
            await self._with_raw_response.get_live_event_thumbnail_alt1(
                live_event_id, thumbnail_id, request_options=request_options
            ),
        )

    async def get_live_event_thumbnail_alt2(
        self, live_event_id: float, thumbnail_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Picture:
        """This method returns a single thumbnail image of the specified event.

        Args:
            live_event_id: The ID of the event.
            thumbnail_id: The ID of the thumbnail.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The thumbnail was returned.

        Raises:
            ApiError: Error code 3200: The authenticated user can't access the thumbnail. Error code 5000: No such
                event, thumbnail, or user exists. ``error`` is ``Error | RawError``."""
        return unwrap(
            await self._with_raw_response.get_live_event_thumbnail_alt2(
                live_event_id, thumbnail_id, request_options=request_options
            ),
        )

    async def get_live_event_thumbnails(
        self, live_event_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> PictureConnection:
        """This method returns every thumbnail image of the specified event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The thumbnails were returned.

        Raises:
            ApiError: Error code 5000: No such event or user exists. ``error`` is ``Error | RawError``."""
        return unwrap(
            await self._with_raw_response.get_live_event_thumbnails(
                live_event_id, user_id, request_options=request_options
            ),
        )

    async def get_live_event_thumbnails_alt1(
        self, live_event_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> PictureConnection:
        """This method returns every thumbnail image of the specified event.

        Args:
            live_event_id: The ID of the event.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The thumbnails were returned.

        Raises:
            ApiError: Error code 5000: No such event or user exists. ``error`` is ``Error | RawError``."""
        return unwrap(
            await self._with_raw_response.get_live_event_thumbnails_alt1(live_event_id, request_options=request_options)
        )

    async def get_live_event_thumbnails_alt2(
        self, live_event_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> PictureConnection:
        """This method returns every thumbnail image of the specified event.

        Args:
            live_event_id: The ID of the event.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The thumbnails were returned.

        Raises:
            ApiError: Error code 5000: No such event or user exists. ``error`` is ``Error | RawError``."""
        return unwrap(
            await self._with_raw_response.get_live_event_thumbnails_alt2(live_event_id, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> AsyncLiveEventThumbnailsWithRawResponse:
        return self._with_raw_response


class LiveEventThumbnailsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_live_event_thumbnail(
        self,
        live_event_id: float,
        user_id: float,
        *,
        body: UsersLiveEventsPicturesRequest | UsersLiveEventsPicturesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Picture, CreateLiveEventThumbnailErrorBody]:
        """This method creates a thumbnail image for the specified event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users/{user_id}/live_events/{live_event_id}/pictures"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersLiveEventsPicturesRequest | UsersLiveEventsPicturesRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=create_live_event_thumbnail_error_mapper,
            request_options=request_options,
        )

    def create_live_event_thumbnail_alt1(
        self,
        live_event_id: float,
        *,
        body: LiveEventsPicturesRequest | LiveEventsPicturesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Picture, CreateLiveEventThumbnailAlt1ErrorBody]:
        """This method creates a thumbnail image for the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/live_events/{live_event_id}/pictures"),
            path_params=[param[float]("live_event_id", live_event_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[LiveEventsPicturesRequest | LiveEventsPicturesRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=create_live_event_thumbnail_alt1_error_mapper,
            request_options=request_options,
        )

    def create_live_event_thumbnail_alt2(
        self,
        live_event_id: float,
        *,
        body: MeLiveEventsPicturesRequest | MeLiveEventsPicturesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Picture, CreateLiveEventThumbnailAlt2ErrorBody]:
        """This method creates a thumbnail image for the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/me/live_events/{live_event_id}/pictures"),
            path_params=[param[float]("live_event_id", live_event_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MeLiveEventsPicturesRequest | MeLiveEventsPicturesRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=create_live_event_thumbnail_alt2_error_mapper,
            request_options=request_options,
        )

    def delete_live_event_thumbnail(
        self,
        live_event_id: float,
        thumbnail_id: float,
        user_id: float,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, DeleteLiveEventThumbnailErrorBody]:
        """This method deletes a thumbnail image for the specified event.

        Args:
            live_event_id: The ID of the event.
            thumbnail_id: The ID of the thumbnail.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/users/{user_id}/live_events/{live_event_id}/pictures/{thumbnail_id}"),
            path_params=[
                param[float]("live_event_id", live_event_id),
                param[float]("thumbnail_id", thumbnail_id),
                param[float]("user_id", user_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_live_event_thumbnail_error_mapper,
            request_options=request_options,
        )

    def delete_live_event_thumbnail_alt1(
        self, live_event_id: float, thumbnail_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteLiveEventThumbnailAlt1ErrorBody]:
        """This method deletes a thumbnail image for the specified event.

        Args:
            live_event_id: The ID of the event.
            thumbnail_id: The ID of the thumbnail.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/live_events/{live_event_id}/pictures/{thumbnail_id}"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("thumbnail_id", thumbnail_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_live_event_thumbnail_alt1_error_mapper,
            request_options=request_options,
        )

    def delete_live_event_thumbnail_alt2(
        self, live_event_id: float, thumbnail_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteLiveEventThumbnailAlt2ErrorBody]:
        """This method deletes a thumbnail image for the specified event.

        Args:
            live_event_id: The ID of the event.
            thumbnail_id: The ID of the thumbnail.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/live_events/{live_event_id}/pictures/{thumbnail_id}"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("thumbnail_id", thumbnail_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_live_event_thumbnail_alt2_error_mapper,
            request_options=request_options,
        )

    def edit_live_event_thumbnail(
        self,
        live_event_id: float,
        thumbnail_id: float,
        user_id: float,
        *,
        body: UsersLiveEventsPicturesThumbnailIdRequest | UsersLiveEventsPicturesThumbnailIdRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Picture, EditLiveEventThumbnailErrorBody]:
        """This method edits a thumbnail image for the specified event.

        Args:
            live_event_id: The ID of the event.
            thumbnail_id: The ID of the thumbnail.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/users/{user_id}/live_events/{live_event_id}/pictures/{thumbnail_id}"),
            path_params=[
                param[float]("live_event_id", live_event_id),
                param[float]("thumbnail_id", thumbnail_id),
                param[float]("user_id", user_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[
                UsersLiveEventsPicturesThumbnailIdRequest | UsersLiveEventsPicturesThumbnailIdRequestDict | None
            ](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=edit_live_event_thumbnail_error_mapper,
            request_options=request_options,
        )

    def edit_live_event_thumbnail_alt1(
        self,
        live_event_id: float,
        thumbnail_id: float,
        *,
        body: LiveEventsPicturesRequest | LiveEventsPicturesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Picture, EditLiveEventThumbnailAlt1ErrorBody]:
        """This method edits a thumbnail image for the specified event.

        Args:
            live_event_id: The ID of the event.
            thumbnail_id: The ID of the thumbnail.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/live_events/{live_event_id}/pictures/{thumbnail_id}"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("thumbnail_id", thumbnail_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[LiveEventsPicturesRequest | LiveEventsPicturesRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=edit_live_event_thumbnail_alt1_error_mapper,
            request_options=request_options,
        )

    def edit_live_event_thumbnail_alt2(
        self,
        live_event_id: float,
        thumbnail_id: float,
        *,
        body: MeLiveEventsPicturesRequest | MeLiveEventsPicturesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Picture, EditLiveEventThumbnailAlt2ErrorBody]:
        """This method edits a thumbnail image for the specified event.

        Args:
            live_event_id: The ID of the event.
            thumbnail_id: The ID of the thumbnail.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/me/live_events/{live_event_id}/pictures/{thumbnail_id}"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("thumbnail_id", thumbnail_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MeLiveEventsPicturesRequest | MeLiveEventsPicturesRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=edit_live_event_thumbnail_alt2_error_mapper,
            request_options=request_options,
        )

    def get_live_event_thumbnail(
        self,
        live_event_id: float,
        thumbnail_id: float,
        user_id: float,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Picture, GetLiveEventThumbnailErrorBody]:
        """This method returns a single thumbnail image of the specified event.

        Args:
            live_event_id: The ID of the event.
            thumbnail_id: The ID of the thumbnail.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/live_events/{live_event_id}/pictures/{thumbnail_id}"),
            path_params=[
                param[float]("live_event_id", live_event_id),
                param[float]("thumbnail_id", thumbnail_id),
                param[float]("user_id", user_id),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=get_live_event_thumbnail_error_mapper,
            request_options=request_options,
        )

    def get_live_event_thumbnail_alt1(
        self, live_event_id: float, thumbnail_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Picture, GetLiveEventThumbnailAlt1ErrorBody]:
        """This method returns a single thumbnail image of the specified event.

        Args:
            live_event_id: The ID of the event.
            thumbnail_id: The ID of the thumbnail.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/live_events/{live_event_id}/pictures/{thumbnail_id}"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("thumbnail_id", thumbnail_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=get_live_event_thumbnail_alt1_error_mapper,
            request_options=request_options,
        )

    def get_live_event_thumbnail_alt2(
        self, live_event_id: float, thumbnail_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Picture, GetLiveEventThumbnailAlt2ErrorBody]:
        """This method returns a single thumbnail image of the specified event.

        Args:
            live_event_id: The ID of the event.
            thumbnail_id: The ID of the thumbnail.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/live_events/{live_event_id}/pictures/{thumbnail_id}"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("thumbnail_id", thumbnail_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=get_live_event_thumbnail_alt2_error_mapper,
            request_options=request_options,
        )

    def get_live_event_thumbnails(
        self, live_event_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PictureConnection, GetLiveEventThumbnailsErrorBody]:
        """This method returns every thumbnail image of the specified event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/live_events/{live_event_id}/pictures"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("user_id", user_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[PictureConnection],
            error_mapper=get_live_event_thumbnails_error_mapper,
            request_options=request_options,
        )

    def get_live_event_thumbnails_alt1(
        self, live_event_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PictureConnection, GetLiveEventThumbnailsAlt1ErrorBody]:
        """This method returns every thumbnail image of the specified event.

        Args:
            live_event_id: The ID of the event.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/live_events/{live_event_id}/pictures"),
            path_params=[param[float]("live_event_id", live_event_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[PictureConnection],
            error_mapper=get_live_event_thumbnails_alt1_error_mapper,
            request_options=request_options,
        )

    def get_live_event_thumbnails_alt2(
        self, live_event_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PictureConnection, GetLiveEventThumbnailsAlt2ErrorBody]:
        """This method returns every thumbnail image of the specified event.

        Args:
            live_event_id: The ID of the event.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/live_events/{live_event_id}/pictures"),
            path_params=[param[float]("live_event_id", live_event_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[PictureConnection],
            error_mapper=get_live_event_thumbnails_alt2_error_mapper,
            request_options=request_options,
        )


class AsyncLiveEventThumbnailsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_live_event_thumbnail(
        self,
        live_event_id: float,
        user_id: float,
        *,
        body: UsersLiveEventsPicturesRequest | UsersLiveEventsPicturesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Picture, CreateLiveEventThumbnailErrorBody]:
        """This method creates a thumbnail image for the specified event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users/{user_id}/live_events/{live_event_id}/pictures"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersLiveEventsPicturesRequest | UsersLiveEventsPicturesRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Picture],
            error_mapper=create_live_event_thumbnail_error_mapper,
            request_options=request_options,
        )

    async def create_live_event_thumbnail_alt1(
        self,
        live_event_id: float,
        *,
        body: LiveEventsPicturesRequest | LiveEventsPicturesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Picture, CreateLiveEventThumbnailAlt1ErrorBody]:
        """This method creates a thumbnail image for the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/live_events/{live_event_id}/pictures"),
            path_params=[param[float]("live_event_id", live_event_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[LiveEventsPicturesRequest | LiveEventsPicturesRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Picture],
            error_mapper=create_live_event_thumbnail_alt1_error_mapper,
            request_options=request_options,
        )

    async def create_live_event_thumbnail_alt2(
        self,
        live_event_id: float,
        *,
        body: MeLiveEventsPicturesRequest | MeLiveEventsPicturesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Picture, CreateLiveEventThumbnailAlt2ErrorBody]:
        """This method creates a thumbnail image for the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/me/live_events/{live_event_id}/pictures"),
            path_params=[param[float]("live_event_id", live_event_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MeLiveEventsPicturesRequest | MeLiveEventsPicturesRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Picture],
            error_mapper=create_live_event_thumbnail_alt2_error_mapper,
            request_options=request_options,
        )

    async def delete_live_event_thumbnail(
        self,
        live_event_id: float,
        thumbnail_id: float,
        user_id: float,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, DeleteLiveEventThumbnailErrorBody]:
        """This method deletes a thumbnail image for the specified event.

        Args:
            live_event_id: The ID of the event.
            thumbnail_id: The ID of the thumbnail.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/users/{user_id}/live_events/{live_event_id}/pictures/{thumbnail_id}"),
            path_params=[
                param[float]("live_event_id", live_event_id),
                param[float]("thumbnail_id", thumbnail_id),
                param[float]("user_id", user_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_empty_response,
            error_mapper=delete_live_event_thumbnail_error_mapper,
            request_options=request_options,
        )

    async def delete_live_event_thumbnail_alt1(
        self, live_event_id: float, thumbnail_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteLiveEventThumbnailAlt1ErrorBody]:
        """This method deletes a thumbnail image for the specified event.

        Args:
            live_event_id: The ID of the event.
            thumbnail_id: The ID of the thumbnail.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/live_events/{live_event_id}/pictures/{thumbnail_id}"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("thumbnail_id", thumbnail_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_empty_response,
            error_mapper=delete_live_event_thumbnail_alt1_error_mapper,
            request_options=request_options,
        )

    async def delete_live_event_thumbnail_alt2(
        self, live_event_id: float, thumbnail_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteLiveEventThumbnailAlt2ErrorBody]:
        """This method deletes a thumbnail image for the specified event.

        Args:
            live_event_id: The ID of the event.
            thumbnail_id: The ID of the thumbnail.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/live_events/{live_event_id}/pictures/{thumbnail_id}"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("thumbnail_id", thumbnail_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_empty_response,
            error_mapper=delete_live_event_thumbnail_alt2_error_mapper,
            request_options=request_options,
        )

    async def edit_live_event_thumbnail(
        self,
        live_event_id: float,
        thumbnail_id: float,
        user_id: float,
        *,
        body: UsersLiveEventsPicturesThumbnailIdRequest | UsersLiveEventsPicturesThumbnailIdRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Picture, EditLiveEventThumbnailErrorBody]:
        """This method edits a thumbnail image for the specified event.

        Args:
            live_event_id: The ID of the event.
            thumbnail_id: The ID of the thumbnail.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/users/{user_id}/live_events/{live_event_id}/pictures/{thumbnail_id}"),
            path_params=[
                param[float]("live_event_id", live_event_id),
                param[float]("thumbnail_id", thumbnail_id),
                param[float]("user_id", user_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[
                UsersLiveEventsPicturesThumbnailIdRequest | UsersLiveEventsPicturesThumbnailIdRequestDict | None
            ](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Picture],
            error_mapper=edit_live_event_thumbnail_error_mapper,
            request_options=request_options,
        )

    async def edit_live_event_thumbnail_alt1(
        self,
        live_event_id: float,
        thumbnail_id: float,
        *,
        body: LiveEventsPicturesRequest | LiveEventsPicturesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Picture, EditLiveEventThumbnailAlt1ErrorBody]:
        """This method edits a thumbnail image for the specified event.

        Args:
            live_event_id: The ID of the event.
            thumbnail_id: The ID of the thumbnail.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/live_events/{live_event_id}/pictures/{thumbnail_id}"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("thumbnail_id", thumbnail_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[LiveEventsPicturesRequest | LiveEventsPicturesRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Picture],
            error_mapper=edit_live_event_thumbnail_alt1_error_mapper,
            request_options=request_options,
        )

    async def edit_live_event_thumbnail_alt2(
        self,
        live_event_id: float,
        thumbnail_id: float,
        *,
        body: MeLiveEventsPicturesRequest | MeLiveEventsPicturesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Picture, EditLiveEventThumbnailAlt2ErrorBody]:
        """This method edits a thumbnail image for the specified event.

        Args:
            live_event_id: The ID of the event.
            thumbnail_id: The ID of the thumbnail.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/me/live_events/{live_event_id}/pictures/{thumbnail_id}"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("thumbnail_id", thumbnail_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MeLiveEventsPicturesRequest | MeLiveEventsPicturesRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Picture],
            error_mapper=edit_live_event_thumbnail_alt2_error_mapper,
            request_options=request_options,
        )

    async def get_live_event_thumbnail(
        self,
        live_event_id: float,
        thumbnail_id: float,
        user_id: float,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Picture, GetLiveEventThumbnailErrorBody]:
        """This method returns a single thumbnail image of the specified event.

        Args:
            live_event_id: The ID of the event.
            thumbnail_id: The ID of the thumbnail.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/live_events/{live_event_id}/pictures/{thumbnail_id}"),
            path_params=[
                param[float]("live_event_id", live_event_id),
                param[float]("thumbnail_id", thumbnail_id),
                param[float]("user_id", user_id),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Picture],
            error_mapper=get_live_event_thumbnail_error_mapper,
            request_options=request_options,
        )

    async def get_live_event_thumbnail_alt1(
        self, live_event_id: float, thumbnail_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Picture, GetLiveEventThumbnailAlt1ErrorBody]:
        """This method returns a single thumbnail image of the specified event.

        Args:
            live_event_id: The ID of the event.
            thumbnail_id: The ID of the thumbnail.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/live_events/{live_event_id}/pictures/{thumbnail_id}"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("thumbnail_id", thumbnail_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Picture],
            error_mapper=get_live_event_thumbnail_alt1_error_mapper,
            request_options=request_options,
        )

    async def get_live_event_thumbnail_alt2(
        self, live_event_id: float, thumbnail_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Picture, GetLiveEventThumbnailAlt2ErrorBody]:
        """This method returns a single thumbnail image of the specified event.

        Args:
            live_event_id: The ID of the event.
            thumbnail_id: The ID of the thumbnail.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/live_events/{live_event_id}/pictures/{thumbnail_id}"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("thumbnail_id", thumbnail_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Picture],
            error_mapper=get_live_event_thumbnail_alt2_error_mapper,
            request_options=request_options,
        )

    async def get_live_event_thumbnails(
        self, live_event_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PictureConnection, GetLiveEventThumbnailsErrorBody]:
        """This method returns every thumbnail image of the specified event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/live_events/{live_event_id}/pictures"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("user_id", user_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[PictureConnection],
            error_mapper=get_live_event_thumbnails_error_mapper,
            request_options=request_options,
        )

    async def get_live_event_thumbnails_alt1(
        self, live_event_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PictureConnection, GetLiveEventThumbnailsAlt1ErrorBody]:
        """This method returns every thumbnail image of the specified event.

        Args:
            live_event_id: The ID of the event.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/live_events/{live_event_id}/pictures"),
            path_params=[param[float]("live_event_id", live_event_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[PictureConnection],
            error_mapper=get_live_event_thumbnails_alt1_error_mapper,
            request_options=request_options,
        )

    async def get_live_event_thumbnails_alt2(
        self, live_event_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PictureConnection, GetLiveEventThumbnailsAlt2ErrorBody]:
        """This method returns every thumbnail image of the specified event.

        Args:
            live_event_id: The ID of the event.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/live_events/{live_event_id}/pictures"),
            path_params=[param[float]("live_event_id", live_event_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[PictureConnection],
            error_mapper=get_live_event_thumbnails_alt2_error_mapper,
            request_options=request_options,
        )
