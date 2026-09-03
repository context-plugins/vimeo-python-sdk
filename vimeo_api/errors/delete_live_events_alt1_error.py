from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

DeleteLiveEventsAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _DeleteLiveEventsAlt1Error:
    def map(self, response: HttpResponse) -> DeleteLiveEventsAlt1ErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


delete_live_events_alt1_error_mapper: Final[ErrorMapper[DeleteLiveEventsAlt1ErrorBody]] = _DeleteLiveEventsAlt1Error()
