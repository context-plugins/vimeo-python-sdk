from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetTranscriptMetadataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetTranscriptMetadataError:
    def map(self, response: HttpResponse) -> GetTranscriptMetadataErrorBody:
        match response.status_code:
            case 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_transcript_metadata_error_mapper: Final[ErrorMapper[GetTranscriptMetadataErrorBody]] = _GetTranscriptMetadataError()
