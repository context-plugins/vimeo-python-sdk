from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.legacy_error import LegacyError

AddVideoTagErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _AddVideoTagError:
    def map(self, status_code: int, content: bytes) -> AddVideoTagErrorBody:
        match status_code:
            case 400 | 403:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


add_video_tag_error_mapper: Final[ErrorMapper[AddVideoTagErrorBody]] = _AddVideoTagError()
