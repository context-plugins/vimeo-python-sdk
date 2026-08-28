from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

CreateLiveEventThumbnailAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _CreateLiveEventThumbnailAlt1Error:
    def map(self, response: HttpResponse) -> CreateLiveEventThumbnailAlt1ErrorBody:
        match response.status_code:
            case 403 | 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


create_live_event_thumbnail_alt1_error_mapper: Final[
    ErrorMapper[CreateLiveEventThumbnailAlt1ErrorBody]
] = _CreateLiveEventThumbnailAlt1Error()
