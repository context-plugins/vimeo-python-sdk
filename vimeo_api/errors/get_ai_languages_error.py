from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

GetAiLanguagesErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetAiLanguagesError:
    def map(self, status_code: int, content: bytes) -> GetAiLanguagesErrorBody:
        match status_code:
            case 400:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


get_ai_languages_error_mapper: Final[ErrorMapper[GetAiLanguagesErrorBody]] = _GetAiLanguagesError()
