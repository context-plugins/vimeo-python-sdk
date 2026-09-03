from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetLiveEventThumbnailsErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetLiveEventThumbnailsError:
    def map(self, response: HttpResponse) -> GetLiveEventThumbnailsErrorBody:
        match response.status_code:
            case 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_live_event_thumbnails_error_mapper: Final[
    ErrorMapper[GetLiveEventThumbnailsErrorBody]
] = _GetLiveEventThumbnailsError()
