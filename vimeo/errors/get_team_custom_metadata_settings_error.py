from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error
from ..models.legacy_error import LegacyError

GetTeamCustomMetadataSettingsErrorBody: TypeAlias = LegacyError | Error | RawError


@dataclass(frozen=True, slots=True)
class _GetTeamCustomMetadataSettingsError:
    def map(self, response: HttpResponse) -> GetTeamCustomMetadataSettingsErrorBody:
        match response.status_code:
            case 401 | 403:
                return decode_json[LegacyError](response)
            case 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_team_custom_metadata_settings_error_mapper: Final[
    ErrorMapper[GetTeamCustomMetadataSettingsErrorBody]
] = _GetTeamCustomMetadataSettingsError()
