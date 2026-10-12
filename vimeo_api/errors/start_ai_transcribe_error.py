from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error
from ..models.legacy_error import LegacyError

StartAiTranscribeErrorBody: TypeAlias = Error | LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _StartAiTranscribeError:
    def map(self, status_code: int, content: bytes) -> StartAiTranscribeErrorBody:
        match status_code:
            case 400 | 403:
                return decode_json[Error](content)
            case 404:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


start_ai_transcribe_error_mapper: Final[ErrorMapper[StartAiTranscribeErrorBody]] = _StartAiTranscribeError()
