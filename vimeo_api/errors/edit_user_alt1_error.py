from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

EditUserAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _EditUserAlt1Error:
    def map(self, status_code: int, content: bytes) -> EditUserAlt1ErrorBody:
        match status_code:
            case 400:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


edit_user_alt1_error_mapper: Final[ErrorMapper[EditUserAlt1ErrorBody]] = _EditUserAlt1Error()
