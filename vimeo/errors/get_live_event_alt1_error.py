from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetLiveEventAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetLiveEventAlt1Error:
    def map(self, response: HttpResponse) -> GetLiveEventAlt1ErrorBody:
        match response.status_code:
            case 400 | 401 | 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_live_event_alt1_error_mapper: Final[ErrorMapper[GetLiveEventAlt1ErrorBody]] = _GetLiveEventAlt1Error()
