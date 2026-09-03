from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetLiveEventVideosErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetLiveEventVideosError:
    def map(self, response: HttpResponse) -> GetLiveEventVideosErrorBody:
        match response.status_code:
            case 400 | 401 | 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_live_event_videos_error_mapper: Final[ErrorMapper[GetLiveEventVideosErrorBody]] = _GetLiveEventVideosError()
