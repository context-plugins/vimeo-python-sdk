from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

GetLiveEventVideoAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetLiveEventVideoAlt1Error:
    def map(self, status_code: int, content: bytes) -> GetLiveEventVideoAlt1ErrorBody:
        match status_code:
            case 400 | 401 | 404:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


get_live_event_video_alt1_error_mapper: Final[
    ErrorMapper[GetLiveEventVideoAlt1ErrorBody]
] = _GetLiveEventVideoAlt1Error()
