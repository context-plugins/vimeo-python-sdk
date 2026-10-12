from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error
from ..models.legacy_error import LegacyError

GetAiTranscribeStatusErrorBody: TypeAlias = Error | LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _GetAiTranscribeStatusError:
    def map(self, status_code: int, content: bytes) -> GetAiTranscribeStatusErrorBody:
        match status_code:
            case 403:
                return decode_json[Error](content)
            case 404:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


get_ai_transcribe_status_error_mapper: Final[
    ErrorMapper[GetAiTranscribeStatusErrorBody]
] = _GetAiTranscribeStatusError()
