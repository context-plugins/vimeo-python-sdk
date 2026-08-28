from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

DeleteLiveEventsErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _DeleteLiveEventsError:
    def map(self, response: HttpResponse) -> DeleteLiveEventsErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


delete_live_events_error_mapper: Final[ErrorMapper[DeleteLiveEventsErrorBody]] = _DeleteLiveEventsError()
