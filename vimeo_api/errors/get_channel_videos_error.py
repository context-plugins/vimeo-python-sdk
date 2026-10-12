from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.legacy_error import LegacyError

GetChannelVideosErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _GetChannelVideosError:
    def map(self, status_code: int, content: bytes) -> GetChannelVideosErrorBody:
        match status_code:
            case 400 | 404:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


get_channel_videos_error_mapper: Final[ErrorMapper[GetChannelVideosErrorBody]] = _GetChannelVideosError()
