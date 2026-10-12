from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.legacy_error import LegacyError

GetVodBackgroundsErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _GetVodBackgroundsError:
    def map(self, status_code: int, content: bytes) -> GetVodBackgroundsErrorBody:
        match status_code:
            case 404:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


get_vod_backgrounds_error_mapper: Final[ErrorMapper[GetVodBackgroundsErrorBody]] = _GetVodBackgroundsError()
