from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

GetLiveEventVideosAlt2ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetLiveEventVideosAlt2Error:
    def map(self, status_code: int, content: bytes) -> GetLiveEventVideosAlt2ErrorBody:
        match status_code:
            case 400 | 401 | 404:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


get_live_event_videos_alt2_error_mapper: Final[
    ErrorMapper[GetLiveEventVideosAlt2ErrorBody]
] = _GetLiveEventVideosAlt2Error()
