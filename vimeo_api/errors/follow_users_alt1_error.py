from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

FollowUsersAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _FollowUsersAlt1Error:
    def map(self, status_code: int, content: bytes) -> FollowUsersAlt1ErrorBody:
        match status_code:
            case 400 | 401 | 403 | 429 | 500:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


follow_users_alt1_error_mapper: Final[ErrorMapper[FollowUsersAlt1ErrorBody]] = _FollowUsersAlt1Error()
