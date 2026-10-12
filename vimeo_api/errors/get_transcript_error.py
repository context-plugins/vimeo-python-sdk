from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

GetTranscriptErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetTranscriptError:
    def map(self, status_code: int, content: bytes) -> GetTranscriptErrorBody:
        match status_code:
            case 404:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


get_transcript_error_mapper: Final[ErrorMapper[GetTranscriptErrorBody]] = _GetTranscriptError()
