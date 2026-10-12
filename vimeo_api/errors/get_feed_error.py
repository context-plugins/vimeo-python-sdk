from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

GetFeedErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetFeedError:
    def map(self, status_code: int, content: bytes) -> GetFeedErrorBody:
        match status_code:
            case 404:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


get_feed_error_mapper: Final[ErrorMapper[GetFeedErrorBody]] = _GetFeedError()
