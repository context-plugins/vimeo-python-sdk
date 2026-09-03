from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

UpdateLiveEventDestinationErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _UpdateLiveEventDestinationError:
    def map(self, response: HttpResponse) -> UpdateLiveEventDestinationErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


update_live_event_destination_error_mapper: Final[
    ErrorMapper[UpdateLiveEventDestinationErrorBody]
] = _UpdateLiveEventDestinationError()
