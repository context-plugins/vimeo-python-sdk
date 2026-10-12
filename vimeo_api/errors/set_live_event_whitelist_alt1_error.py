from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

SetLiveEventWhitelistAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _SetLiveEventWhitelistAlt1Error:
    def map(self, status_code: int, content: bytes) -> SetLiveEventWhitelistAlt1ErrorBody:
        match status_code:
            case 400 | 403 | 404 | 500:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


set_live_event_whitelist_alt1_error_mapper: Final[
    ErrorMapper[SetLiveEventWhitelistAlt1ErrorBody]
] = _SetLiveEventWhitelistAlt1Error()
