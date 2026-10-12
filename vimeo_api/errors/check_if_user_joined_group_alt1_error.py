from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.legacy_error import LegacyError

CheckIfUserJoinedGroupAlt1ErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _CheckIfUserJoinedGroupAlt1Error:
    def map(self, status_code: int, content: bytes) -> CheckIfUserJoinedGroupAlt1ErrorBody:
        match status_code:
            case 404:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


check_if_user_joined_group_alt1_error_mapper: Final[
    ErrorMapper[CheckIfUserJoinedGroupAlt1ErrorBody]
] = _CheckIfUserJoinedGroupAlt1Error()
