from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

DeleteFolderEmbedPresetErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _DeleteFolderEmbedPresetError:
    def map(self, response: HttpResponse) -> DeleteFolderEmbedPresetErrorBody:
        match response.status_code:
            case 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


delete_folder_embed_preset_error_mapper: Final[
    ErrorMapper[DeleteFolderEmbedPresetErrorBody]
] = _DeleteFolderEmbedPresetError()
