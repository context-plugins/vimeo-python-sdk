from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

GetLiveEventWhitelistErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetLiveEventWhitelistError:
    def map(self, status_code: int, content: bytes) -> GetLiveEventWhitelistErrorBody:
        match status_code:
            case 400 | 403 | 404 | 500:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


get_live_event_whitelist_error_mapper: Final[
    ErrorMapper[GetLiveEventWhitelistErrorBody]
] = _GetLiveEventWhitelistError()
