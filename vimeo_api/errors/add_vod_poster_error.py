from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.legacy_error import LegacyError

AddVodPosterErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _AddVodPosterError:
    def map(self, status_code: int, content: bytes) -> AddVodPosterErrorBody:
        match status_code:
            case 403:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


add_vod_poster_error_mapper: Final[ErrorMapper[AddVodPosterErrorBody]] = _AddVodPosterError()
