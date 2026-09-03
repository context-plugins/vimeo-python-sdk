from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

GetShowcasesAlt1ErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _GetShowcasesAlt1Error:
    def map(self, response: HttpResponse) -> GetShowcasesAlt1ErrorBody:
        match response.status_code:
            case 400:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


get_showcases_alt1_error_mapper: Final[ErrorMapper[GetShowcasesAlt1ErrorBody]] = _GetShowcasesAlt1Error()
