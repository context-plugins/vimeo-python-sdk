from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.legacy_error import LegacyError

EditEmbedPresetAlt1ErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _EditEmbedPresetAlt1Error:
    def map(self, status_code: int, content: bytes) -> EditEmbedPresetAlt1ErrorBody:
        match status_code:
            case 400 | 404:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


edit_embed_preset_alt1_error_mapper: Final[ErrorMapper[EditEmbedPresetAlt1ErrorBody]] = _EditEmbedPresetAlt1Error()
