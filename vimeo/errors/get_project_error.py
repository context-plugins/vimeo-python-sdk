from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetProjectErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetProjectError:
    def map(self, response: HttpResponse) -> GetProjectErrorBody:
        match response.status_code:
            case 401 | 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_project_error_mapper: Final[ErrorMapper[GetProjectErrorBody]] = _GetProjectError()
