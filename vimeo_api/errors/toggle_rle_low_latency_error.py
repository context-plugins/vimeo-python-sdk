from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

ToggleRleLowLatencyErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _ToggleRleLowLatencyError:
    def map(self, status_code: int, content: bytes) -> ToggleRleLowLatencyErrorBody:
        match status_code:
            case 403 | 404:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


toggle_rle_low_latency_error_mapper: Final[ErrorMapper[ToggleRleLowLatencyErrorBody]] = _ToggleRleLowLatencyError()
