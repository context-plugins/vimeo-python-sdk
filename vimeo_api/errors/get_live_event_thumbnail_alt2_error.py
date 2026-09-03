from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetLiveEventThumbnailAlt2ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetLiveEventThumbnailAlt2Error:
    def map(self, response: HttpResponse) -> GetLiveEventThumbnailAlt2ErrorBody:
        match response.status_code:
            case 403 | 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_live_event_thumbnail_alt2_error_mapper: Final[
    ErrorMapper[GetLiveEventThumbnailAlt2ErrorBody]
] = _GetLiveEventThumbnailAlt2Error()
