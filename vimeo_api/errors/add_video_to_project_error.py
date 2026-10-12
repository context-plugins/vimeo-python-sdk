from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

AddVideoToProjectErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _AddVideoToProjectError:
    def map(self, status_code: int, content: bytes) -> AddVideoToProjectErrorBody:
        match status_code:
            case 404:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


add_video_to_project_error_mapper: Final[ErrorMapper[AddVideoToProjectErrorBody]] = _AddVideoToProjectError()
