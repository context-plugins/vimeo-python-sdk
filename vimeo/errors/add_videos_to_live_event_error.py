from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

AddVideosToLiveEventErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _AddVideosToLiveEventError:
    def map(self, response: HttpResponse) -> AddVideosToLiveEventErrorBody:
        match response.status_code:
            case 400 | 403 | 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


add_videos_to_live_event_error_mapper: Final[ErrorMapper[AddVideosToLiveEventErrorBody]] = _AddVideosToLiveEventError()
