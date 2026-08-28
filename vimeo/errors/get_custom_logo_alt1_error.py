from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

GetCustomLogoAlt1ErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _GetCustomLogoAlt1Error:
    def map(self, response: HttpResponse) -> GetCustomLogoAlt1ErrorBody:
        match response.status_code:
            case 403:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


get_custom_logo_alt1_error_mapper: Final[ErrorMapper[GetCustomLogoAlt1ErrorBody]] = _GetCustomLogoAlt1Error()
