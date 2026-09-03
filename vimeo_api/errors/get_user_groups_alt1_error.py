from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetUserGroupsAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetUserGroupsAlt1Error:
    def map(self, response: HttpResponse) -> GetUserGroupsAlt1ErrorBody:
        match response.status_code:
            case 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_user_groups_alt1_error_mapper: Final[ErrorMapper[GetUserGroupsAlt1ErrorBody]] = _GetUserGroupsAlt1Error()
