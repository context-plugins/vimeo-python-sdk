from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

EndLiveEventAlt2ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _EndLiveEventAlt2Error:
    def map(self, status_code: int, content: bytes) -> EndLiveEventAlt2ErrorBody:
        match status_code:
            case 400 | 403 | 404 | 500:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


end_live_event_alt2_error_mapper: Final[ErrorMapper[EndLiveEventAlt2ErrorBody]] = _EndLiveEventAlt2Error()
