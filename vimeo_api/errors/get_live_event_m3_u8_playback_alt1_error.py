from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

GetLiveEventM3U8PlaybackAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetLiveEventM3U8PlaybackAlt1Error:
    def map(self, status_code: int, content: bytes) -> GetLiveEventM3U8PlaybackAlt1ErrorBody:
        match status_code:
            case 400 | 401 | 403 | 404 | 500 | 503:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


get_live_event_m3_u8_playback_alt1_error_mapper: Final[
    ErrorMapper[GetLiveEventM3U8PlaybackAlt1ErrorBody]
] = _GetLiveEventM3U8PlaybackAlt1Error()
