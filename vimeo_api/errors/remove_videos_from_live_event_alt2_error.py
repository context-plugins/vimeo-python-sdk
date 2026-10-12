from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

RemoveVideosFromLiveEventAlt2ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _RemoveVideosFromLiveEventAlt2Error:
    def map(self, status_code: int, content: bytes) -> RemoveVideosFromLiveEventAlt2ErrorBody:
        match status_code:
            case 400 | 403 | 404:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


remove_videos_from_live_event_alt2_error_mapper: Final[
    ErrorMapper[RemoveVideosFromLiveEventAlt2ErrorBody]
] = _RemoveVideosFromLiveEventAlt2Error()
