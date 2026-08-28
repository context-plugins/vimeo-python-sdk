from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error
from ..models.legacy_error import LegacyError

StartAiTranscribeErrorBody: TypeAlias = Error | LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _StartAiTranscribeError:
    def map(self, response: HttpResponse) -> StartAiTranscribeErrorBody:
        match response.status_code:
            case 400 | 403:
                return decode_json[Error](response)
            case 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


start_ai_transcribe_error_mapper: Final[ErrorMapper[StartAiTranscribeErrorBody]] = _StartAiTranscribeError()
