from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

FollowUsersErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _FollowUsersError:
    def map(self, response: HttpResponse) -> FollowUsersErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 429 | 500:
                return decode_json[Error](response)
            case _:
                return RawError(response)


follow_users_error_mapper: Final[ErrorMapper[FollowUsersErrorBody]] = _FollowUsersError()
