from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.legacy_error import LegacyError

CreateCustomLogoErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _CreateCustomLogoError:
    def map(self, status_code: int, content: bytes) -> CreateCustomLogoErrorBody:
        match status_code:
            case 403:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


create_custom_logo_error_mapper: Final[ErrorMapper[CreateCustomLogoErrorBody]] = _CreateCustomLogoError()
