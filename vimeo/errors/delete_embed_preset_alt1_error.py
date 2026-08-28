from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

DeleteEmbedPresetAlt1ErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _DeleteEmbedPresetAlt1Error:
    def map(self, response: HttpResponse) -> DeleteEmbedPresetAlt1ErrorBody:
        match response.status_code:
            case 403:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


delete_embed_preset_alt1_error_mapper: Final[
    ErrorMapper[DeleteEmbedPresetAlt1ErrorBody]
] = _DeleteEmbedPresetAlt1Error()
