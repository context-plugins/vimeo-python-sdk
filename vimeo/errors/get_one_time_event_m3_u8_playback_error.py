from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetOneTimeEventM3U8PlaybackErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetOneTimeEventM3U8PlaybackError:
    def map(self, response: HttpResponse) -> GetOneTimeEventM3U8PlaybackErrorBody:
        match response.status_code:
            case 401 | 403 | 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_one_time_event_m3_u8_playback_error_mapper: Final[
    ErrorMapper[GetOneTimeEventM3U8PlaybackErrorBody]
] = _GetOneTimeEventM3U8PlaybackError()
