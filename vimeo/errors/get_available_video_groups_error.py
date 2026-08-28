from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetAvailableVideoGroupsErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetAvailableVideoGroupsError:
    def map(self, response: HttpResponse) -> GetAvailableVideoGroupsErrorBody:
        match response.status_code:
            case 403 | 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_available_video_groups_error_mapper: Final[
    ErrorMapper[GetAvailableVideoGroupsErrorBody]
] = _GetAvailableVideoGroupsError()
