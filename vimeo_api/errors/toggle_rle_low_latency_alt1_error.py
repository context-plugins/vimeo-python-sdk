from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

ToggleRleLowLatencyAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _ToggleRleLowLatencyAlt1Error:
    def map(self, status_code: int, content: bytes) -> ToggleRleLowLatencyAlt1ErrorBody:
        match status_code:
            case 403 | 404:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


toggle_rle_low_latency_alt1_error_mapper: Final[
    ErrorMapper[ToggleRleLowLatencyAlt1ErrorBody]
] = _ToggleRleLowLatencyAlt1Error()
