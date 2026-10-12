from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

UpdateLiveEventErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _UpdateLiveEventError:
    def map(self, status_code: int, content: bytes) -> UpdateLiveEventErrorBody:
        match status_code:
            case 400 | 403 | 404:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


update_live_event_error_mapper: Final[ErrorMapper[UpdateLiveEventErrorBody]] = _UpdateLiveEventError()
