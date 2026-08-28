from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

ToggleRleLowLatencyErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _ToggleRleLowLatencyError:
    def map(self, response: HttpResponse) -> ToggleRleLowLatencyErrorBody:
        match response.status_code:
            case 403 | 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


toggle_rle_low_latency_error_mapper: Final[ErrorMapper[ToggleRleLowLatencyErrorBody]] = _ToggleRleLowLatencyError()
