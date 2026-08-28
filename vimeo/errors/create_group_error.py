from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error
from ..models.legacy_error import LegacyError

CreateGroupErrorBody: TypeAlias = LegacyError | Error | RawError


@dataclass(frozen=True, slots=True)
class _CreateGroupError:
    def map(self, response: HttpResponse) -> CreateGroupErrorBody:
        match response.status_code:
            case 400 | 403:
                return decode_json[LegacyError](response)
            case 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


create_group_error_mapper: Final[ErrorMapper[CreateGroupErrorBody]] = _CreateGroupError()
