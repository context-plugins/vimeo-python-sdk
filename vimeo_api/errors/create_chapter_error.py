from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.legacy_error import LegacyError

CreateChapterErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _CreateChapterError:
    def map(self, status_code: int, content: bytes) -> CreateChapterErrorBody:
        match status_code:
            case 403:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


create_chapter_error_mapper: Final[ErrorMapper[CreateChapterErrorBody]] = _CreateChapterError()
