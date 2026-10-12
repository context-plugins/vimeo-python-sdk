from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

GetProjectVideosAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetProjectVideosAlt1Error:
    def map(self, status_code: int, content: bytes) -> GetProjectVideosAlt1ErrorBody:
        match status_code:
            case 401 | 404:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


get_project_videos_alt1_error_mapper: Final[ErrorMapper[GetProjectVideosAlt1ErrorBody]] = _GetProjectVideosAlt1Error()
