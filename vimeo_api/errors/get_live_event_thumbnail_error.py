from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetLiveEventThumbnailErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetLiveEventThumbnailError:
    def map(self, response: HttpResponse) -> GetLiveEventThumbnailErrorBody:
        match response.status_code:
            case 403 | 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_live_event_thumbnail_error_mapper: Final[
    ErrorMapper[GetLiveEventThumbnailErrorBody]
] = _GetLiveEventThumbnailError()
