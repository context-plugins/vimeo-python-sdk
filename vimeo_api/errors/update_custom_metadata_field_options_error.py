from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error
from ..models.legacy_error import LegacyError

UpdateCustomMetadataFieldOptionsErrorBody: TypeAlias = Error | LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _UpdateCustomMetadataFieldOptionsError:
    def map(self, status_code: int, content: bytes) -> UpdateCustomMetadataFieldOptionsErrorBody:
        match status_code:
            case 400:
                return decode_json[Error](content)
            case 401 | 403:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


update_custom_metadata_field_options_error_mapper: Final[
    ErrorMapper[UpdateCustomMetadataFieldOptionsErrorBody]
] = _UpdateCustomMetadataFieldOptionsError()
