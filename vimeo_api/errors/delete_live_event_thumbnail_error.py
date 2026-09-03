from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

DeleteLiveEventThumbnailErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _DeleteLiveEventThumbnailError:
    def map(self, response: HttpResponse) -> DeleteLiveEventThumbnailErrorBody:
        match response.status_code:
            case 403 | 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


delete_live_event_thumbnail_error_mapper: Final[
    ErrorMapper[DeleteLiveEventThumbnailErrorBody]
] = _DeleteLiveEventThumbnailError()
