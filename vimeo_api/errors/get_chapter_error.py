from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.legacy_error import LegacyError

GetChapterErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _GetChapterError:
    def map(self, status_code: int, content: bytes) -> GetChapterErrorBody:
        match status_code:
            case 404:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


get_chapter_error_mapper: Final[ErrorMapper[GetChapterErrorBody]] = _GetChapterError()
