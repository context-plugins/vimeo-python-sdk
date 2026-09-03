from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetAiLanguagesErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetAiLanguagesError:
    def map(self, response: HttpResponse) -> GetAiLanguagesErrorBody:
        match response.status_code:
            case 400:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_ai_languages_error_mapper: Final[ErrorMapper[GetAiLanguagesErrorBody]] = _GetAiLanguagesError()
