from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

SetLiveEventWhitelistErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _SetLiveEventWhitelistError:
    def map(self, response: HttpResponse) -> SetLiveEventWhitelistErrorBody:
        match response.status_code:
            case 400 | 403 | 404 | 500:
                return decode_json[Error](response)
            case _:
                return RawError(response)


set_live_event_whitelist_error_mapper: Final[
    ErrorMapper[SetLiveEventWhitelistErrorBody]
] = _SetLiveEventWhitelistError()
