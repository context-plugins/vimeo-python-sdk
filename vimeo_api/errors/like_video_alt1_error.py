from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.legacy_error import LegacyError

LikeVideoAlt1ErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _LikeVideoAlt1Error:
    def map(self, status_code: int, content: bytes) -> LikeVideoAlt1ErrorBody:
        match status_code:
            case 400 | 403:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


like_video_alt1_error_mapper: Final[ErrorMapper[LikeVideoAlt1ErrorBody]] = _LikeVideoAlt1Error()
