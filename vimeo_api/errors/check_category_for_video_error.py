from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.legacy_error import LegacyError

CheckCategoryForVideoErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _CheckCategoryForVideoError:
    def map(self, status_code: int, content: bytes) -> CheckCategoryForVideoErrorBody:
        match status_code:
            case 404:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


check_category_for_video_error_mapper: Final[
    ErrorMapper[CheckCategoryForVideoErrorBody]
] = _CheckCategoryForVideoError()
