from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

GetLiveEventThumbnailsAlt2ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetLiveEventThumbnailsAlt2Error:
    def map(self, status_code: int, content: bytes) -> GetLiveEventThumbnailsAlt2ErrorBody:
        match status_code:
            case 404:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


get_live_event_thumbnails_alt2_error_mapper: Final[
    ErrorMapper[GetLiveEventThumbnailsAlt2ErrorBody]
] = _GetLiveEventThumbnailsAlt2Error()
