from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetLiveEventThumbnailsAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetLiveEventThumbnailsAlt1Error:
    def map(self, response: HttpResponse) -> GetLiveEventThumbnailsAlt1ErrorBody:
        match response.status_code:
            case 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_live_event_thumbnails_alt1_error_mapper: Final[
    ErrorMapper[GetLiveEventThumbnailsAlt1ErrorBody]
] = _GetLiveEventThumbnailsAlt1Error()
