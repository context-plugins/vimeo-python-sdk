from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.legacy_error import LegacyError

CreateShowcaseAlt1ErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _CreateShowcaseAlt1Error:
    def map(self, status_code: int, content: bytes) -> CreateShowcaseAlt1ErrorBody:
        match status_code:
            case 400 | 403:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


create_showcase_alt1_error_mapper: Final[ErrorMapper[CreateShowcaseAlt1ErrorBody]] = _CreateShowcaseAlt1Error()
