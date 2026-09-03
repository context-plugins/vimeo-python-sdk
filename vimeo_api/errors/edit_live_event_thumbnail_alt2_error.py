from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

EditLiveEventThumbnailAlt2ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _EditLiveEventThumbnailAlt2Error:
    def map(self, response: HttpResponse) -> EditLiveEventThumbnailAlt2ErrorBody:
        match response.status_code:
            case 403 | 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


edit_live_event_thumbnail_alt2_error_mapper: Final[
    ErrorMapper[EditLiveEventThumbnailAlt2ErrorBody]
] = _EditLiveEventThumbnailAlt2Error()
