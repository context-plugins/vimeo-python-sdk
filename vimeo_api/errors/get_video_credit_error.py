from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.legacy_error import LegacyError

GetVideoCreditErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _GetVideoCreditError:
    def map(self, status_code: int, content: bytes) -> GetVideoCreditErrorBody:
        match status_code:
            case 404:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


get_video_credit_error_mapper: Final[ErrorMapper[GetVideoCreditErrorBody]] = _GetVideoCreditError()
