from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

GetLiveEventThumbnailsAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetLiveEventThumbnailsAlt1Error:
    def map(self, status_code: int, content: bytes) -> GetLiveEventThumbnailsAlt1ErrorBody:
        match status_code:
            case 404:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


get_live_event_thumbnails_alt1_error_mapper: Final[
    ErrorMapper[GetLiveEventThumbnailsAlt1ErrorBody]
] = _GetLiveEventThumbnailsAlt1Error()
