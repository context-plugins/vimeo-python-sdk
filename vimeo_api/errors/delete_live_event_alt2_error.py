from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

DeleteLiveEventAlt2ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _DeleteLiveEventAlt2Error:
    def map(self, response: HttpResponse) -> DeleteLiveEventAlt2ErrorBody:
        match response.status_code:
            case 403 | 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


delete_live_event_alt2_error_mapper: Final[ErrorMapper[DeleteLiveEventAlt2ErrorBody]] = _DeleteLiveEventAlt2Error()
