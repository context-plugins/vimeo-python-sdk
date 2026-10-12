from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.legacy_error import LegacyError

EditTextTrackErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _EditTextTrackError:
    def map(self, status_code: int, content: bytes) -> EditTextTrackErrorBody:
        match status_code:
            case 403 | 404:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


edit_text_track_error_mapper: Final[ErrorMapper[EditTextTrackErrorBody]] = _EditTextTrackError()
