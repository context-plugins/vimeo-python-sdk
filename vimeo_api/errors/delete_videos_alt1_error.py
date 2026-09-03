from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

DeleteVideosAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _DeleteVideosAlt1Error:
    def map(self, response: HttpResponse) -> DeleteVideosAlt1ErrorBody:
        match response.status_code:
            case 400 | 401 | 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


delete_videos_alt1_error_mapper: Final[ErrorMapper[DeleteVideosAlt1ErrorBody]] = _DeleteVideosAlt1Error()
