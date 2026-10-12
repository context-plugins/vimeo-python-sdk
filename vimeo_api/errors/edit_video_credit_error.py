from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.legacy_error import LegacyError

EditVideoCreditErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _EditVideoCreditError:
    def map(self, status_code: int, content: bytes) -> EditVideoCreditErrorBody:
        match status_code:
            case 400 | 404:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


edit_video_credit_error_mapper: Final[ErrorMapper[EditVideoCreditErrorBody]] = _EditVideoCreditError()
