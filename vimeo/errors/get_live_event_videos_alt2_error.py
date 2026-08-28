from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetLiveEventVideosAlt2ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetLiveEventVideosAlt2Error:
    def map(self, response: HttpResponse) -> GetLiveEventVideosAlt2ErrorBody:
        match response.status_code:
            case 400 | 401 | 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_live_event_videos_alt2_error_mapper: Final[
    ErrorMapper[GetLiveEventVideosAlt2ErrorBody]
] = _GetLiveEventVideosAlt2Error()
