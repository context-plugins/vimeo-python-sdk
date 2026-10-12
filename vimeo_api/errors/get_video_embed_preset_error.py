from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.legacy_error import LegacyError

GetVideoEmbedPresetErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _GetVideoEmbedPresetError:
    def map(self, status_code: int, content: bytes) -> GetVideoEmbedPresetErrorBody:
        match status_code:
            case 404:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


get_video_embed_preset_error_mapper: Final[ErrorMapper[GetVideoEmbedPresetErrorBody]] = _GetVideoEmbedPresetError()
