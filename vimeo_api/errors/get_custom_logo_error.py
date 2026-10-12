from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.legacy_error import LegacyError

GetCustomLogoErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _GetCustomLogoError:
    def map(self, status_code: int, content: bytes) -> GetCustomLogoErrorBody:
        match status_code:
            case 403:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


get_custom_logo_error_mapper: Final[ErrorMapper[GetCustomLogoErrorBody]] = _GetCustomLogoError()
