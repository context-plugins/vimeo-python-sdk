from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.legacy_error import LegacyError

CopyVideoAlt2ErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _CopyVideoAlt2Error:
    def map(self, status_code: int, content: bytes) -> CopyVideoAlt2ErrorBody:
        match status_code:
            case 403 | 404:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


copy_video_alt2_error_mapper: Final[ErrorMapper[CopyVideoAlt2ErrorBody]] = _CopyVideoAlt2Error()
