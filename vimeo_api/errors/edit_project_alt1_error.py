from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

EditProjectAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _EditProjectAlt1Error:
    def map(self, status_code: int, content: bytes) -> EditProjectAlt1ErrorBody:
        match status_code:
            case 400 | 401 | 403 | 404:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


edit_project_alt1_error_mapper: Final[ErrorMapper[EditProjectAlt1ErrorBody]] = _EditProjectAlt1Error()
