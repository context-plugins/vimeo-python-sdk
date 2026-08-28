from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

AddVideoToProjectAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _AddVideoToProjectAlt1Error:
    def map(self, response: HttpResponse) -> AddVideoToProjectAlt1ErrorBody:
        match response.status_code:
            case 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


add_video_to_project_alt1_error_mapper: Final[
    ErrorMapper[AddVideoToProjectAlt1ErrorBody]
] = _AddVideoToProjectAlt1Error()
