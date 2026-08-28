from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetAppearancesAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetAppearancesAlt1Error:
    def map(self, response: HttpResponse) -> GetAppearancesAlt1ErrorBody:
        match response.status_code:
            case 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_appearances_alt1_error_mapper: Final[ErrorMapper[GetAppearancesAlt1ErrorBody]] = _GetAppearancesAlt1Error()
