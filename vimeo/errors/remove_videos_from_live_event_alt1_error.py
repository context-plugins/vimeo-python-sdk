from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

RemoveVideosFromLiveEventAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _RemoveVideosFromLiveEventAlt1Error:
    def map(self, response: HttpResponse) -> RemoveVideosFromLiveEventAlt1ErrorBody:
        match response.status_code:
            case 400 | 403 | 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


remove_videos_from_live_event_alt1_error_mapper: Final[
    ErrorMapper[RemoveVideosFromLiveEventAlt1ErrorBody]
] = _RemoveVideosFromLiveEventAlt1Error()
