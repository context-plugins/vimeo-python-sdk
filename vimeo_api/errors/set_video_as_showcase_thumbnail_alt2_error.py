from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

SetVideoAsShowcaseThumbnailAlt2ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _SetVideoAsShowcaseThumbnailAlt2Error:
    def map(self, response: HttpResponse) -> SetVideoAsShowcaseThumbnailAlt2ErrorBody:
        match response.status_code:
            case 403 | 404 | 500:
                return decode_json[Error](response)
            case _:
                return RawError(response)


set_video_as_showcase_thumbnail_alt2_error_mapper: Final[
    ErrorMapper[SetVideoAsShowcaseThumbnailAlt2ErrorBody]
] = _SetVideoAsShowcaseThumbnailAlt2Error()
