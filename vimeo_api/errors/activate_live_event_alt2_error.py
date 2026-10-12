from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

ActivateLiveEventAlt2ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _ActivateLiveEventAlt2Error:
    def map(self, status_code: int, content: bytes) -> ActivateLiveEventAlt2ErrorBody:
        match status_code:
            case 400 | 401 | 403 | 404 | 500 | 503:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


activate_live_event_alt2_error_mapper: Final[
    ErrorMapper[ActivateLiveEventAlt2ErrorBody]
] = _ActivateLiveEventAlt2Error()
