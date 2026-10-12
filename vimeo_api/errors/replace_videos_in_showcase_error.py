from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.legacy_error import LegacyError

ReplaceVideosInShowcaseErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _ReplaceVideosInShowcaseError:
    def map(self, status_code: int, content: bytes) -> ReplaceVideosInShowcaseErrorBody:
        match status_code:
            case 403 | 404:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


replace_videos_in_showcase_error_mapper: Final[
    ErrorMapper[ReplaceVideosInShowcaseErrorBody]
] = _ReplaceVideosInShowcaseError()
