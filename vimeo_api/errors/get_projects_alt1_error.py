from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

GetProjectsAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetProjectsAlt1Error:
    def map(self, status_code: int, content: bytes) -> GetProjectsAlt1ErrorBody:
        match status_code:
            case 401:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


get_projects_alt1_error_mapper: Final[ErrorMapper[GetProjectsAlt1ErrorBody]] = _GetProjectsAlt1Error()
