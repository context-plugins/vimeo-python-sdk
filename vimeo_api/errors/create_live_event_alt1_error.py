from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

CreateLiveEventAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _CreateLiveEventAlt1Error:
    def map(self, response: HttpResponse) -> CreateLiveEventAlt1ErrorBody:
        match response.status_code:
            case 400 | 401 | 403:
                return decode_json[Error](response)
            case _:
                return RawError(response)


create_live_event_alt1_error_mapper: Final[ErrorMapper[CreateLiveEventAlt1ErrorBody]] = _CreateLiveEventAlt1Error()
