from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

AddVideosToLiveEventAlt2ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _AddVideosToLiveEventAlt2Error:
    def map(self, response: HttpResponse) -> AddVideosToLiveEventAlt2ErrorBody:
        match response.status_code:
            case 400 | 403 | 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


add_videos_to_live_event_alt2_error_mapper: Final[
    ErrorMapper[AddVideosToLiveEventAlt2ErrorBody]
] = _AddVideosToLiveEventAlt2Error()
