from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.legacy_error import LegacyError

DeleteVideoCreditErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _DeleteVideoCreditError:
    def map(self, status_code: int, content: bytes) -> DeleteVideoCreditErrorBody:
        match status_code:
            case 400:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


delete_video_credit_error_mapper: Final[ErrorMapper[DeleteVideoCreditErrorBody]] = _DeleteVideoCreditError()
