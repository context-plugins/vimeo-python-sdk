from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetLiveEventThumbnailAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetLiveEventThumbnailAlt1Error:
    def map(self, response: HttpResponse) -> GetLiveEventThumbnailAlt1ErrorBody:
        match response.status_code:
            case 403 | 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_live_event_thumbnail_alt1_error_mapper: Final[
    ErrorMapper[GetLiveEventThumbnailAlt1ErrorBody]
] = _GetLiveEventThumbnailAlt1Error()
