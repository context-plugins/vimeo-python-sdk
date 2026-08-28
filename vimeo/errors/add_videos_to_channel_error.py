from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

AddVideosToChannelErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _AddVideosToChannelError:
    def map(self, response: HttpResponse) -> AddVideosToChannelErrorBody:
        match response.status_code:
            case 403 | 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


add_videos_to_channel_error_mapper: Final[ErrorMapper[AddVideosToChannelErrorBody]] = _AddVideosToChannelError()
