from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

CreateLiveEventThumbnailAlt2ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _CreateLiveEventThumbnailAlt2Error:
    def map(self, status_code: int, content: bytes) -> CreateLiveEventThumbnailAlt2ErrorBody:
        match status_code:
            case 403 | 404:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


create_live_event_thumbnail_alt2_error_mapper: Final[
    ErrorMapper[CreateLiveEventThumbnailAlt2ErrorBody]
] = _CreateLiveEventThumbnailAlt2Error()
