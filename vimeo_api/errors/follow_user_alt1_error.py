from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

FollowUserAlt1ErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _FollowUserAlt1Error:
    def map(self, response: HttpResponse) -> FollowUserAlt1ErrorBody:
        match response.status_code:
            case 403:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


follow_user_alt1_error_mapper: Final[ErrorMapper[FollowUserAlt1ErrorBody]] = _FollowUserAlt1Error()
