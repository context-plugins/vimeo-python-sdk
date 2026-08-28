from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error
from ..models.legacy_error import LegacyError

GetTeamCustomMetadataIncompleteVideosErrorBody: TypeAlias = Error | LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _GetTeamCustomMetadataIncompleteVideosError:
    def map(self, response: HttpResponse) -> GetTeamCustomMetadataIncompleteVideosErrorBody:
        match response.status_code:
            case 400:
                return decode_json[Error](response)
            case 401 | 403:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


get_team_custom_metadata_incomplete_videos_error_mapper: Final[
    ErrorMapper[GetTeamCustomMetadataIncompleteVideosErrorBody]
] = _GetTeamCustomMetadataIncompleteVideosError()
