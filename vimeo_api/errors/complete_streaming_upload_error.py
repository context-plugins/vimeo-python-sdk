from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

CompleteStreamingUploadErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _CompleteStreamingUploadError:
    def map(self, status_code: int, content: bytes) -> CompleteStreamingUploadErrorBody:
        match status_code:
            case 400 | 404 | 500:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


complete_streaming_upload_error_mapper: Final[
    ErrorMapper[CompleteStreamingUploadErrorBody]
] = _CompleteStreamingUploadError()
