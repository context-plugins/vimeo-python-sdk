from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.legacy_error import LegacyError

CheckIfUserIsFollowingAlt1ErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _CheckIfUserIsFollowingAlt1Error:
    def map(self, status_code: int, content: bytes) -> CheckIfUserIsFollowingAlt1ErrorBody:
        match status_code:
            case 404:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


check_if_user_is_following_alt1_error_mapper: Final[
    ErrorMapper[CheckIfUserIsFollowingAlt1ErrorBody]
] = _CheckIfUserIsFollowingAlt1Error()
