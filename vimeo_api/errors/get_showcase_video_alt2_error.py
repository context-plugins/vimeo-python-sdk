from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.legacy_error import LegacyError

GetShowcaseVideoAlt2ErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _GetShowcaseVideoAlt2Error:
    def map(self, status_code: int, content: bytes) -> GetShowcaseVideoAlt2ErrorBody:
        match status_code:
            case 404:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


get_showcase_video_alt2_error_mapper: Final[ErrorMapper[GetShowcaseVideoAlt2ErrorBody]] = _GetShowcaseVideoAlt2Error()
