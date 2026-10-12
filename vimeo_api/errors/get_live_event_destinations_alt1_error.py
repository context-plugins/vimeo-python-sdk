from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

GetLiveEventDestinationsAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetLiveEventDestinationsAlt1Error:
    def map(self, status_code: int, content: bytes) -> GetLiveEventDestinationsAlt1ErrorBody:
        match status_code:
            case 400 | 401 | 403 | 404:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


get_live_event_destinations_alt1_error_mapper: Final[
    ErrorMapper[GetLiveEventDestinationsAlt1ErrorBody]
] = _GetLiveEventDestinationsAlt1Error()
