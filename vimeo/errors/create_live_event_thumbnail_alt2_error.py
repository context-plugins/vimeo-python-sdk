from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

CreateLiveEventThumbnailAlt2ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _CreateLiveEventThumbnailAlt2Error:
    def map(self, response: HttpResponse) -> CreateLiveEventThumbnailAlt2ErrorBody:
        match response.status_code:
            case 403 | 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


create_live_event_thumbnail_alt2_error_mapper: Final[
    ErrorMapper[CreateLiveEventThumbnailAlt2ErrorBody]
] = _CreateLiveEventThumbnailAlt2Error()
