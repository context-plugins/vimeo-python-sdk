from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

CreateLiveEventThumbnailErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _CreateLiveEventThumbnailError:
    def map(self, status_code: int, content: bytes) -> CreateLiveEventThumbnailErrorBody:
        match status_code:
            case 403 | 404:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


create_live_event_thumbnail_error_mapper: Final[
    ErrorMapper[CreateLiveEventThumbnailErrorBody]
] = _CreateLiveEventThumbnailError()
