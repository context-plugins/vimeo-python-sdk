from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error
from ..models.legacy_error import LegacyError

UpdateVideoCustomMetadataErrorBody: TypeAlias = Error | LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _UpdateVideoCustomMetadataError:
    def map(self, response: HttpResponse) -> UpdateVideoCustomMetadataErrorBody:
        match response.status_code:
            case 400:
                return decode_json[Error](response)
            case 401 | 403 | 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


update_video_custom_metadata_error_mapper: Final[
    ErrorMapper[UpdateVideoCustomMetadataErrorBody]
] = _UpdateVideoCustomMetadataError()
