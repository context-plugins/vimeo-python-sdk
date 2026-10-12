from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

GetUserGroupsAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetUserGroupsAlt1Error:
    def map(self, status_code: int, content: bytes) -> GetUserGroupsAlt1ErrorBody:
        match status_code:
            case 404:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


get_user_groups_alt1_error_mapper: Final[ErrorMapper[GetUserGroupsAlt1ErrorBody]] = _GetUserGroupsAlt1Error()
