from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

GetCustomLogosAlt1ErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _GetCustomLogosAlt1Error:
    def map(self, response: HttpResponse) -> GetCustomLogosAlt1ErrorBody:
        match response.status_code:
            case 403:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


get_custom_logos_alt1_error_mapper: Final[ErrorMapper[GetCustomLogosAlt1ErrorBody]] = _GetCustomLogosAlt1Error()
