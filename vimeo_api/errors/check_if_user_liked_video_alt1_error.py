from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.legacy_error import LegacyError

CheckIfUserLikedVideoAlt1ErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _CheckIfUserLikedVideoAlt1Error:
    def map(self, status_code: int, content: bytes) -> CheckIfUserLikedVideoAlt1ErrorBody:
        match status_code:
            case 404:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


check_if_user_liked_video_alt1_error_mapper: Final[
    ErrorMapper[CheckIfUserLikedVideoAlt1ErrorBody]
] = _CheckIfUserLikedVideoAlt1Error()
