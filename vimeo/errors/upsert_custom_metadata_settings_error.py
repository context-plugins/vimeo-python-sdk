from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error
from ..models.legacy_error import LegacyError

UpsertCustomMetadataSettingsErrorBody: TypeAlias = Error | LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _UpsertCustomMetadataSettingsError:
    def map(self, response: HttpResponse) -> UpsertCustomMetadataSettingsErrorBody:
        match response.status_code:
            case 400:
                return decode_json[Error](response)
            case 401 | 403:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


upsert_custom_metadata_settings_error_mapper: Final[
    ErrorMapper[UpsertCustomMetadataSettingsErrorBody]
] = _UpsertCustomMetadataSettingsError()
