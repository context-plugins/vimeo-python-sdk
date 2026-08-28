from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

SetVideoAsShowcaseFeaturedAlt2ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _SetVideoAsShowcaseFeaturedAlt2Error:
    def map(self, response: HttpResponse) -> SetVideoAsShowcaseFeaturedAlt2ErrorBody:
        match response.status_code:
            case 403 | 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


set_video_as_showcase_featured_alt2_error_mapper: Final[
    ErrorMapper[SetVideoAsShowcaseFeaturedAlt2ErrorBody]
] = _SetVideoAsShowcaseFeaturedAlt2Error()
