from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.legacy_error import LegacyError

GetCustomLogoAlt1ErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _GetCustomLogoAlt1Error:
    def map(self, status_code: int, content: bytes) -> GetCustomLogoAlt1ErrorBody:
        match status_code:
            case 403:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


get_custom_logo_alt1_error_mapper: Final[ErrorMapper[GetCustomLogoAlt1ErrorBody]] = _GetCustomLogoAlt1Error()
