from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

ToggleRleLowLatencyAlt2ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _ToggleRleLowLatencyAlt2Error:
    def map(self, status_code: int, content: bytes) -> ToggleRleLowLatencyAlt2ErrorBody:
        match status_code:
            case 403 | 404:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


toggle_rle_low_latency_alt2_error_mapper: Final[
    ErrorMapper[ToggleRleLowLatencyAlt2ErrorBody]
] = _ToggleRleLowLatencyAlt2Error()
