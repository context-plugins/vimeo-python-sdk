from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

DeleteProjectAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _DeleteProjectAlt1Error:
    def map(self, status_code: int, content: bytes) -> DeleteProjectAlt1ErrorBody:
        match status_code:
            case 401 | 403 | 404:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


delete_project_alt1_error_mapper: Final[ErrorMapper[DeleteProjectAlt1ErrorBody]] = _DeleteProjectAlt1Error()
