from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetLiveEventDestinationsAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetLiveEventDestinationsAlt1Error:
    def map(self, response: HttpResponse) -> GetLiveEventDestinationsAlt1ErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_live_event_destinations_alt1_error_mapper: Final[
    ErrorMapper[GetLiveEventDestinationsAlt1ErrorBody]
] = _GetLiveEventDestinationsAlt1Error()
