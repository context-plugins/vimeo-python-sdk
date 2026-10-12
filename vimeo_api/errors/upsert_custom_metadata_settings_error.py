from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error
from ..models.legacy_error import LegacyError

UpsertCustomMetadataSettingsErrorBody: TypeAlias = Error | LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _UpsertCustomMetadataSettingsError:
    def map(self, status_code: int, content: bytes) -> UpsertCustomMetadataSettingsErrorBody:
        match status_code:
            case 400:
                return decode_json[Error](content)
            case 401 | 403:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


upsert_custom_metadata_settings_error_mapper: Final[
    ErrorMapper[UpsertCustomMetadataSettingsErrorBody]
] = _UpsertCustomMetadataSettingsError()
