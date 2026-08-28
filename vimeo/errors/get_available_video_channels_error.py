from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

GetAvailableVideoChannelsErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _GetAvailableVideoChannelsError:
    def map(self, response: HttpResponse) -> GetAvailableVideoChannelsErrorBody:
        match response.status_code:
            case 403 | 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


get_available_video_channels_error_mapper: Final[
    ErrorMapper[GetAvailableVideoChannelsErrorBody]
] = _GetAvailableVideoChannelsError()
