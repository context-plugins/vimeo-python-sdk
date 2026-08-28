from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

CheckIfUserJoinedGroupErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _CheckIfUserJoinedGroupError:
    def map(self, response: HttpResponse) -> CheckIfUserJoinedGroupErrorBody:
        match response.status_code:
            case 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


check_if_user_joined_group_error_mapper: Final[
    ErrorMapper[CheckIfUserJoinedGroupErrorBody]
] = _CheckIfUserJoinedGroupError()
