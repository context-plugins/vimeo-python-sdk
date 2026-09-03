from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

EndLiveEventErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _EndLiveEventError:
    def map(self, response: HttpResponse) -> EndLiveEventErrorBody:
        match response.status_code:
            case 400 | 403 | 404 | 500:
                return decode_json[Error](response)
            case _:
                return RawError(response)


end_live_event_error_mapper: Final[ErrorMapper[EndLiveEventErrorBody]] = _EndLiveEventError()
