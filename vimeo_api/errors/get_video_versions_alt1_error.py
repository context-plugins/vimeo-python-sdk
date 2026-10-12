from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error
from ..models.legacy_error import LegacyError

GetVideoVersionsAlt1ErrorBody: TypeAlias = Error | LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _GetVideoVersionsAlt1Error:
    def map(self, status_code: int, content: bytes) -> GetVideoVersionsAlt1ErrorBody:
        match status_code:
            case 401:
                return decode_json[Error](content)
            case 404:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


get_video_versions_alt1_error_mapper: Final[ErrorMapper[GetVideoVersionsAlt1ErrorBody]] = _GetVideoVersionsAlt1Error()
