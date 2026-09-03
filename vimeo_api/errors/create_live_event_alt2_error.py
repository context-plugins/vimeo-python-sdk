from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

CreateLiveEventAlt2ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _CreateLiveEventAlt2Error:
    def map(self, response: HttpResponse) -> CreateLiveEventAlt2ErrorBody:
        match response.status_code:
            case 400 | 401 | 403:
                return decode_json[Error](response)
            case _:
                return RawError(response)


create_live_event_alt2_error_mapper: Final[ErrorMapper[CreateLiveEventAlt2ErrorBody]] = _CreateLiveEventAlt2Error()
