from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetProjectsAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetProjectsAlt1Error:
    def map(self, response: HttpResponse) -> GetProjectsAlt1ErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_projects_alt1_error_mapper: Final[ErrorMapper[GetProjectsAlt1ErrorBody]] = _GetProjectsAlt1Error()
