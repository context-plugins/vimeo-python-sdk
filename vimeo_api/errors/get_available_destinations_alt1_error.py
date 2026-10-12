from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

GetAvailableDestinationsAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetAvailableDestinationsAlt1Error:
    def map(self, status_code: int, content: bytes) -> GetAvailableDestinationsAlt1ErrorBody:
        match status_code:
            case 401 | 403:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


get_available_destinations_alt1_error_mapper: Final[
    ErrorMapper[GetAvailableDestinationsAlt1ErrorBody]
] = _GetAvailableDestinationsAlt1Error()
