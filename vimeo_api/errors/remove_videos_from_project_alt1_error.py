from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

RemoveVideosFromProjectAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _RemoveVideosFromProjectAlt1Error:
    def map(self, response: HttpResponse) -> RemoveVideosFromProjectAlt1ErrorBody:
        match response.status_code:
            case 400 | 401 | 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


remove_videos_from_project_alt1_error_mapper: Final[
    ErrorMapper[RemoveVideosFromProjectAlt1ErrorBody]
] = _RemoveVideosFromProjectAlt1Error()
