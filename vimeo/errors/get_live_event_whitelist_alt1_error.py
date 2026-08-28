from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetLiveEventWhitelistAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetLiveEventWhitelistAlt1Error:
    def map(self, response: HttpResponse) -> GetLiveEventWhitelistAlt1ErrorBody:
        match response.status_code:
            case 400 | 403 | 404 | 500:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_live_event_whitelist_alt1_error_mapper: Final[
    ErrorMapper[GetLiveEventWhitelistAlt1ErrorBody]
] = _GetLiveEventWhitelistAlt1Error()
