from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

ClipTrimErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _ClipTrimError:
    def map(self, status_code: int, content: bytes) -> ClipTrimErrorBody:
        match status_code:
            case 401 | 403:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


clip_trim_error_mapper: Final[ErrorMapper[ClipTrimErrorBody]] = _ClipTrimError()
