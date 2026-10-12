from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

AddVideosToLiveEventAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _AddVideosToLiveEventAlt1Error:
    def map(self, status_code: int, content: bytes) -> AddVideosToLiveEventAlt1ErrorBody:
        match status_code:
            case 400 | 403 | 404:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


add_videos_to_live_event_alt1_error_mapper: Final[
    ErrorMapper[AddVideosToLiveEventAlt1ErrorBody]
] = _AddVideosToLiveEventAlt1Error()
