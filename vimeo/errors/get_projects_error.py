from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetProjectsErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetProjectsError:
    def map(self, response: HttpResponse) -> GetProjectsErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_projects_error_mapper: Final[ErrorMapper[GetProjectsErrorBody]] = _GetProjectsError()
