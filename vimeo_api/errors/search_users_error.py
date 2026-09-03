from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error
from ..models.legacy_error import LegacyError

SearchUsersErrorBody: TypeAlias = Error | LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _SearchUsersError:
    def map(self, response: HttpResponse) -> SearchUsersErrorBody:
        match response.status_code:
            case 404:
                return decode_json[Error](response)
            case 500 | 503:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


search_users_error_mapper: Final[ErrorMapper[SearchUsersErrorBody]] = _SearchUsersError()
