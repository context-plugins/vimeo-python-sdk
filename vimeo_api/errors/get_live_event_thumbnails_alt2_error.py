from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetLiveEventThumbnailsAlt2ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetLiveEventThumbnailsAlt2Error:
    def map(self, response: HttpResponse) -> GetLiveEventThumbnailsAlt2ErrorBody:
        match response.status_code:
            case 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_live_event_thumbnails_alt2_error_mapper: Final[
    ErrorMapper[GetLiveEventThumbnailsAlt2ErrorBody]
] = _GetLiveEventThumbnailsAlt2Error()
