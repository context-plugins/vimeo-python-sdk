from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

ToggleRleLowLatencyAlt2ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _ToggleRleLowLatencyAlt2Error:
    def map(self, response: HttpResponse) -> ToggleRleLowLatencyAlt2ErrorBody:
        match response.status_code:
            case 403 | 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


toggle_rle_low_latency_alt2_error_mapper: Final[
    ErrorMapper[ToggleRleLowLatencyAlt2ErrorBody]
] = _ToggleRleLowLatencyAlt2Error()
