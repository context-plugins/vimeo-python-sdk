from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

GetAvailableVideoGroupsErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetAvailableVideoGroupsError:
    def map(self, status_code: int, content: bytes) -> GetAvailableVideoGroupsErrorBody:
        match status_code:
            case 403 | 404:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


get_available_video_groups_error_mapper: Final[
    ErrorMapper[GetAvailableVideoGroupsErrorBody]
] = _GetAvailableVideoGroupsError()
