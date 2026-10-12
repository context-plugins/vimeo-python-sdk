from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.legacy_error import LegacyError

GetTextTracksAlt1ErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _GetTextTracksAlt1Error:
    def map(self, status_code: int, content: bytes) -> GetTextTracksAlt1ErrorBody:
        match status_code:
            case 404:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


get_text_tracks_alt1_error_mapper: Final[ErrorMapper[GetTextTracksAlt1ErrorBody]] = _GetTextTracksAlt1Error()
