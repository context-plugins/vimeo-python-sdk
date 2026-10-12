from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.legacy_error import LegacyError

CheckIfUserIsFollowingErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _CheckIfUserIsFollowingError:
    def map(self, status_code: int, content: bytes) -> CheckIfUserIsFollowingErrorBody:
        match status_code:
            case 404:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


check_if_user_is_following_error_mapper: Final[
    ErrorMapper[CheckIfUserIsFollowingErrorBody]
] = _CheckIfUserIsFollowingError()
