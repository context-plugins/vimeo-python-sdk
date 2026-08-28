from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

DeleteVideosErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _DeleteVideosError:
    def map(self, response: HttpResponse) -> DeleteVideosErrorBody:
        match response.status_code:
            case 400 | 401 | 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


delete_videos_error_mapper: Final[ErrorMapper[DeleteVideosErrorBody]] = _DeleteVideosError()
