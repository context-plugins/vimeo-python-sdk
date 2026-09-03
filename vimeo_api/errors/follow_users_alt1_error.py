from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

FollowUsersAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _FollowUsersAlt1Error:
    def map(self, response: HttpResponse) -> FollowUsersAlt1ErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 429 | 500:
                return decode_json[Error](response)
            case _:
                return RawError(response)


follow_users_alt1_error_mapper: Final[ErrorMapper[FollowUsersAlt1ErrorBody]] = _FollowUsersAlt1Error()
