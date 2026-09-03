from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

CreateProjectAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _CreateProjectAlt1Error:
    def map(self, response: HttpResponse) -> CreateProjectAlt1ErrorBody:
        match response.status_code:
            case 400 | 401 | 403:
                return decode_json[Error](response)
            case _:
                return RawError(response)


create_project_alt1_error_mapper: Final[ErrorMapper[CreateProjectAlt1ErrorBody]] = _CreateProjectAlt1Error()
