from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

SetVideoAsShowcaseFeaturedAlt2ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _SetVideoAsShowcaseFeaturedAlt2Error:
    def map(self, status_code: int, content: bytes) -> SetVideoAsShowcaseFeaturedAlt2ErrorBody:
        match status_code:
            case 403 | 404:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


set_video_as_showcase_featured_alt2_error_mapper: Final[
    ErrorMapper[SetVideoAsShowcaseFeaturedAlt2ErrorBody]
] = _SetVideoAsShowcaseFeaturedAlt2Error()
