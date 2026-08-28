from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetLiveEventM3U8PlaybackAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetLiveEventM3U8PlaybackAlt1Error:
    def map(self, response: HttpResponse) -> GetLiveEventM3U8PlaybackAlt1ErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404 | 500 | 503:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_live_event_m3_u8_playback_alt1_error_mapper: Final[
    ErrorMapper[GetLiveEventM3U8PlaybackAlt1ErrorBody]
] = _GetLiveEventM3U8PlaybackAlt1Error()
