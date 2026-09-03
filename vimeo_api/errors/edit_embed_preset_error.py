from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

EditEmbedPresetErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _EditEmbedPresetError:
    def map(self, response: HttpResponse) -> EditEmbedPresetErrorBody:
        match response.status_code:
            case 400 | 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


edit_embed_preset_error_mapper: Final[ErrorMapper[EditEmbedPresetErrorBody]] = _EditEmbedPresetError()
