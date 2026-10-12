from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.legacy_error import LegacyError

AddVodGenreErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _AddVodGenreError:
    def map(self, status_code: int, content: bytes) -> AddVodGenreErrorBody:
        match status_code:
            case 400 | 403 | 404:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


add_vod_genre_error_mapper: Final[ErrorMapper[AddVodGenreErrorBody]] = _AddVodGenreError()
