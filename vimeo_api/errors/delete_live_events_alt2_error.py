from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

DeleteLiveEventsAlt2ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _DeleteLiveEventsAlt2Error:
    def map(self, status_code: int, content: bytes) -> DeleteLiveEventsAlt2ErrorBody:
        match status_code:
            case 401:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


delete_live_events_alt2_error_mapper: Final[ErrorMapper[DeleteLiveEventsAlt2ErrorBody]] = _DeleteLiveEventsAlt2Error()
