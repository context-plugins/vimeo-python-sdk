from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

EditLiveEventThumbnailAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _EditLiveEventThumbnailAlt1Error:
    def map(self, status_code: int, content: bytes) -> EditLiveEventThumbnailAlt1ErrorBody:
        match status_code:
            case 403 | 404:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


edit_live_event_thumbnail_alt1_error_mapper: Final[
    ErrorMapper[EditLiveEventThumbnailAlt1ErrorBody]
] = _EditLiveEventThumbnailAlt1Error()
