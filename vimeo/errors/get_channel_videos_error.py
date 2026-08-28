from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

GetChannelVideosErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _GetChannelVideosError:
    def map(self, response: HttpResponse) -> GetChannelVideosErrorBody:
        match response.status_code:
            case 400 | 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


get_channel_videos_error_mapper: Final[ErrorMapper[GetChannelVideosErrorBody]] = _GetChannelVideosError()
