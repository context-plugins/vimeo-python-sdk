from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

GetLikesAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetLikesAlt1Error:
    def map(self, status_code: int, content: bytes) -> GetLikesAlt1ErrorBody:
        match status_code:
            case 404:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


get_likes_alt1_error_mapper: Final[ErrorMapper[GetLikesAlt1ErrorBody]] = _GetLikesAlt1Error()
