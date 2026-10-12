from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.legacy_error import LegacyError

EditVodErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _EditVodError:
    def map(self, status_code: int, content: bytes) -> EditVodErrorBody:
        match status_code:
            case 403 | 404:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


edit_vod_error_mapper: Final[ErrorMapper[EditVodErrorBody]] = _EditVodError()
