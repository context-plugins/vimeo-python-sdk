from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.legacy_error import LegacyError

ReplaceShowcaseCustomThumbErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _ReplaceShowcaseCustomThumbError:
    def map(self, status_code: int, content: bytes) -> ReplaceShowcaseCustomThumbErrorBody:
        match status_code:
            case 403 | 404:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


replace_showcase_custom_thumb_error_mapper: Final[
    ErrorMapper[ReplaceShowcaseCustomThumbErrorBody]
] = _ReplaceShowcaseCustomThumbError()
