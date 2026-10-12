from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error
from ..models.legacy_error import LegacyError

UpdateVideoCustomMetadataErrorBody: TypeAlias = Error | LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _UpdateVideoCustomMetadataError:
    def map(self, status_code: int, content: bytes) -> UpdateVideoCustomMetadataErrorBody:
        match status_code:
            case 400:
                return decode_json[Error](content)
            case 401 | 403 | 404:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


update_video_custom_metadata_error_mapper: Final[
    ErrorMapper[UpdateVideoCustomMetadataErrorBody]
] = _UpdateVideoCustomMetadataError()
