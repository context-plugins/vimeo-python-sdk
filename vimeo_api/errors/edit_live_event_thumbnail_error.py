from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

EditLiveEventThumbnailErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _EditLiveEventThumbnailError:
    def map(self, response: HttpResponse) -> EditLiveEventThumbnailErrorBody:
        match response.status_code:
            case 403 | 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


edit_live_event_thumbnail_error_mapper: Final[
    ErrorMapper[EditLiveEventThumbnailErrorBody]
] = _EditLiveEventThumbnailError()
