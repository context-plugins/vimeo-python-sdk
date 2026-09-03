from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

UploadVideoAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _UploadVideoAlt1Error:
    def map(self, response: HttpResponse) -> UploadVideoAlt1ErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 500:
                return decode_json[Error](response)
            case _:
                return RawError(response)


upload_video_alt1_error_mapper: Final[ErrorMapper[UploadVideoAlt1ErrorBody]] = _UploadVideoAlt1Error()
