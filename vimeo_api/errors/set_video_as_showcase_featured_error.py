from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

SetVideoAsShowcaseFeaturedErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _SetVideoAsShowcaseFeaturedError:
    def map(self, status_code: int, content: bytes) -> SetVideoAsShowcaseFeaturedErrorBody:
        match status_code:
            case 403 | 404:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


set_video_as_showcase_featured_error_mapper: Final[
    ErrorMapper[SetVideoAsShowcaseFeaturedErrorBody]
] = _SetVideoAsShowcaseFeaturedError()
