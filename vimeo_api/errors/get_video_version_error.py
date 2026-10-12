from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.legacy_error import LegacyError

GetVideoVersionErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _GetVideoVersionError:
    def map(self, status_code: int, content: bytes) -> GetVideoVersionErrorBody:
        match status_code:
            case 404:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


get_video_version_error_mapper: Final[ErrorMapper[GetVideoVersionErrorBody]] = _GetVideoVersionError()
