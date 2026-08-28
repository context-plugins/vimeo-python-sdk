from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetTranscriptErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetTranscriptError:
    def map(self, response: HttpResponse) -> GetTranscriptErrorBody:
        match response.status_code:
            case 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_transcript_error_mapper: Final[ErrorMapper[GetTranscriptErrorBody]] = _GetTranscriptError()
