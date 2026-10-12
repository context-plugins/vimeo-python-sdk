from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error
from ..models.legacy_error import LegacyError

SearchUsersErrorBody: TypeAlias = Error | LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _SearchUsersError:
    def map(self, status_code: int, content: bytes) -> SearchUsersErrorBody:
        match status_code:
            case 404:
                return decode_json[Error](content)
            case 500 | 503:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


search_users_error_mapper: Final[ErrorMapper[SearchUsersErrorBody]] = _SearchUsersError()
