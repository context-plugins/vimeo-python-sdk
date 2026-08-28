from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

DeleteVideoEmbedPresetErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _DeleteVideoEmbedPresetError:
    def map(self, response: HttpResponse) -> DeleteVideoEmbedPresetErrorBody:
        match response.status_code:
            case 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


delete_video_embed_preset_error_mapper: Final[
    ErrorMapper[DeleteVideoEmbedPresetErrorBody]
] = _DeleteVideoEmbedPresetError()
