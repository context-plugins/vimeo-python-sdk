from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetLiveEventDestinationsErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetLiveEventDestinationsError:
    def map(self, response: HttpResponse) -> GetLiveEventDestinationsErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_live_event_destinations_error_mapper: Final[
    ErrorMapper[GetLiveEventDestinationsErrorBody]
] = _GetLiveEventDestinationsError()
