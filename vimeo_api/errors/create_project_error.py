from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

CreateProjectErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _CreateProjectError:
    def map(self, response: HttpResponse) -> CreateProjectErrorBody:
        match response.status_code:
            case 400 | 401 | 403:
                return decode_json[Error](response)
            case _:
                return RawError(response)


create_project_error_mapper: Final[ErrorMapper[CreateProjectErrorBody]] = _CreateProjectError()
