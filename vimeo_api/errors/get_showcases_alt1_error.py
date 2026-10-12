from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.legacy_error import LegacyError

GetShowcasesAlt1ErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _GetShowcasesAlt1Error:
    def map(self, status_code: int, content: bytes) -> GetShowcasesAlt1ErrorBody:
        match status_code:
            case 400:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


get_showcases_alt1_error_mapper: Final[ErrorMapper[GetShowcasesAlt1ErrorBody]] = _GetShowcasesAlt1Error()
