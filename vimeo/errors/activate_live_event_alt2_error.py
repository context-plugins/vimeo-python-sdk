from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

ActivateLiveEventAlt2ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _ActivateLiveEventAlt2Error:
    def map(self, response: HttpResponse) -> ActivateLiveEventAlt2ErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404 | 500 | 503:
                return decode_json[Error](response)
            case _:
                return RawError(response)


activate_live_event_alt2_error_mapper: Final[
    ErrorMapper[ActivateLiveEventAlt2ErrorBody]
] = _ActivateLiveEventAlt2Error()
