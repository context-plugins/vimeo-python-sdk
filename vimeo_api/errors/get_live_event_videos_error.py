from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

GetLiveEventVideosErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetLiveEventVideosError:
    def map(self, status_code: int, content: bytes) -> GetLiveEventVideosErrorBody:
        match status_code:
            case 400 | 401 | 404:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


get_live_event_videos_error_mapper: Final[ErrorMapper[GetLiveEventVideosErrorBody]] = _GetLiveEventVideosError()
