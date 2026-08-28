from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetAvailableDestinationsAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetAvailableDestinationsAlt1Error:
    def map(self, response: HttpResponse) -> GetAvailableDestinationsAlt1ErrorBody:
        match response.status_code:
            case 401 | 403:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_available_destinations_alt1_error_mapper: Final[
    ErrorMapper[GetAvailableDestinationsAlt1ErrorBody]
] = _GetAvailableDestinationsAlt1Error()
