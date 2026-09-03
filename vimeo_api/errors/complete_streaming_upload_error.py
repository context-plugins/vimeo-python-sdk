from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

CompleteStreamingUploadErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _CompleteStreamingUploadError:
    def map(self, response: HttpResponse) -> CompleteStreamingUploadErrorBody:
        match response.status_code:
            case 400 | 404 | 500:
                return decode_json[Error](response)
            case _:
                return RawError(response)


complete_streaming_upload_error_mapper: Final[
    ErrorMapper[CompleteStreamingUploadErrorBody]
] = _CompleteStreamingUploadError()
