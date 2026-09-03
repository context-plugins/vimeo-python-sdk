from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

EditEmbedPresetAlt1ErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _EditEmbedPresetAlt1Error:
    def map(self, response: HttpResponse) -> EditEmbedPresetAlt1ErrorBody:
        match response.status_code:
            case 400 | 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


edit_embed_preset_alt1_error_mapper: Final[ErrorMapper[EditEmbedPresetAlt1ErrorBody]] = _EditEmbedPresetAlt1Error()
