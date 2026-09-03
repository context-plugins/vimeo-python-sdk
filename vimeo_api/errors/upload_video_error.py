from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

UploadVideoErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _UploadVideoError:
    def map(self, response: HttpResponse) -> UploadVideoErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 500:
                return decode_json[Error](response)
            case _:
                return RawError(response)


upload_video_error_mapper: Final[ErrorMapper[UploadVideoErrorBody]] = _UploadVideoError()
