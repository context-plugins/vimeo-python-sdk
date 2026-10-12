from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

GetLiveEventThumbnailsErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetLiveEventThumbnailsError:
    def map(self, status_code: int, content: bytes) -> GetLiveEventThumbnailsErrorBody:
        match status_code:
            case 404:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


get_live_event_thumbnails_error_mapper: Final[
    ErrorMapper[GetLiveEventThumbnailsErrorBody]
] = _GetLiveEventThumbnailsError()
