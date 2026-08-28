from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

DeleteLiveEventThumbnailAlt2ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _DeleteLiveEventThumbnailAlt2Error:
    def map(self, response: HttpResponse) -> DeleteLiveEventThumbnailAlt2ErrorBody:
        match response.status_code:
            case 403 | 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


delete_live_event_thumbnail_alt2_error_mapper: Final[
    ErrorMapper[DeleteLiveEventThumbnailAlt2ErrorBody]
] = _DeleteLiveEventThumbnailAlt2Error()
