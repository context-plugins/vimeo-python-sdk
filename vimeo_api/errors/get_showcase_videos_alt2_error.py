from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.legacy_error import LegacyError

GetShowcaseVideosAlt2ErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _GetShowcaseVideosAlt2Error:
    def map(self, status_code: int, content: bytes) -> GetShowcaseVideosAlt2ErrorBody:
        match status_code:
            case 404:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


get_showcase_videos_alt2_error_mapper: Final[
    ErrorMapper[GetShowcaseVideosAlt2ErrorBody]
] = _GetShowcaseVideosAlt2Error()
