from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

GetTranscriptMetadataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetTranscriptMetadataError:
    def map(self, status_code: int, content: bytes) -> GetTranscriptMetadataErrorBody:
        match status_code:
            case 404:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


get_transcript_metadata_error_mapper: Final[ErrorMapper[GetTranscriptMetadataErrorBody]] = _GetTranscriptMetadataError()
