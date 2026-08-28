from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetLiveEventM3U8PlaybackErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetLiveEventM3U8PlaybackError:
    def map(self, response: HttpResponse) -> GetLiveEventM3U8PlaybackErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404 | 500 | 503:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_live_event_m3_u8_playback_error_mapper: Final[
    ErrorMapper[GetLiveEventM3U8PlaybackErrorBody]
] = _GetLiveEventM3U8PlaybackError()
