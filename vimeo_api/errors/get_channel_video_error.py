from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

GetChannelVideoErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _GetChannelVideoError:
    def map(self, response: HttpResponse) -> GetChannelVideoErrorBody:
        match response.status_code:
            case 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


get_channel_video_error_mapper: Final[ErrorMapper[GetChannelVideoErrorBody]] = _GetChannelVideoError()
