from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

CreateLiveEventAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _CreateLiveEventAlt1Error:
    def map(self, status_code: int, content: bytes) -> CreateLiveEventAlt1ErrorBody:
        match status_code:
            case 400 | 401 | 403:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


create_live_event_alt1_error_mapper: Final[ErrorMapper[CreateLiveEventAlt1ErrorBody]] = _CreateLiveEventAlt1Error()
