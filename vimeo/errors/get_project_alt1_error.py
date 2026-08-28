from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetProjectAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetProjectAlt1Error:
    def map(self, response: HttpResponse) -> GetProjectAlt1ErrorBody:
        match response.status_code:
            case 401 | 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_project_alt1_error_mapper: Final[ErrorMapper[GetProjectAlt1ErrorBody]] = _GetProjectAlt1Error()
