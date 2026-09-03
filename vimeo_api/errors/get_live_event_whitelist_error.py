from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetLiveEventWhitelistErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetLiveEventWhitelistError:
    def map(self, response: HttpResponse) -> GetLiveEventWhitelistErrorBody:
        match response.status_code:
            case 400 | 403 | 404 | 500:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_live_event_whitelist_error_mapper: Final[
    ErrorMapper[GetLiveEventWhitelistErrorBody]
] = _GetLiveEventWhitelistError()
