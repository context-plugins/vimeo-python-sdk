from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

CreateProjectAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _CreateProjectAlt1Error:
    def map(self, status_code: int, content: bytes) -> CreateProjectAlt1ErrorBody:
        match status_code:
            case 400 | 401 | 403:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


create_project_alt1_error_mapper: Final[ErrorMapper[CreateProjectAlt1ErrorBody]] = _CreateProjectAlt1Error()
