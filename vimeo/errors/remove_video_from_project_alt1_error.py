from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

RemoveVideoFromProjectAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _RemoveVideoFromProjectAlt1Error:
    def map(self, response: HttpResponse) -> RemoveVideoFromProjectAlt1ErrorBody:
        match response.status_code:
            case 400 | 401 | 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


remove_video_from_project_alt1_error_mapper: Final[
    ErrorMapper[RemoveVideoFromProjectAlt1ErrorBody]
] = _RemoveVideoFromProjectAlt1Error()
