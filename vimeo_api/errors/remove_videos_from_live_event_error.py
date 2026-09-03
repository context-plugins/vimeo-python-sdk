from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

RemoveVideosFromLiveEventErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _RemoveVideosFromLiveEventError:
    def map(self, response: HttpResponse) -> RemoveVideosFromLiveEventErrorBody:
        match response.status_code:
            case 400 | 403 | 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


remove_videos_from_live_event_error_mapper: Final[
    ErrorMapper[RemoveVideosFromLiveEventErrorBody]
] = _RemoveVideosFromLiveEventError()
