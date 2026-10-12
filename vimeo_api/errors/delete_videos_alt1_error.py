from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

DeleteVideosAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _DeleteVideosAlt1Error:
    def map(self, status_code: int, content: bytes) -> DeleteVideosAlt1ErrorBody:
        match status_code:
            case 400 | 401 | 404:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


delete_videos_alt1_error_mapper: Final[ErrorMapper[DeleteVideosAlt1ErrorBody]] = _DeleteVideosAlt1Error()
