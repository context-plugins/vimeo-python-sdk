from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

AddVideosToProjectAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _AddVideosToProjectAlt1Error:
    def map(self, response: HttpResponse) -> AddVideosToProjectAlt1ErrorBody:
        match response.status_code:
            case 400 | 401 | 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


add_videos_to_project_alt1_error_mapper: Final[
    ErrorMapper[AddVideosToProjectAlt1ErrorBody]
] = _AddVideosToProjectAlt1Error()
