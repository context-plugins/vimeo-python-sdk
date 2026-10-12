from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

CreateLiveEventDestinationAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _CreateLiveEventDestinationAlt1Error:
    def map(self, status_code: int, content: bytes) -> CreateLiveEventDestinationAlt1ErrorBody:
        match status_code:
            case 400 | 401 | 403 | 404:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


create_live_event_destination_alt1_error_mapper: Final[
    ErrorMapper[CreateLiveEventDestinationAlt1ErrorBody]
] = _CreateLiveEventDestinationAlt1Error()
