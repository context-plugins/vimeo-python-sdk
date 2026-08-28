from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

CreateLiveEventThumbnailErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _CreateLiveEventThumbnailError:
    def map(self, response: HttpResponse) -> CreateLiveEventThumbnailErrorBody:
        match response.status_code:
            case 403 | 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


create_live_event_thumbnail_error_mapper: Final[
    ErrorMapper[CreateLiveEventThumbnailErrorBody]
] = _CreateLiveEventThumbnailError()
