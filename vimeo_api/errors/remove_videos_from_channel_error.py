from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.legacy_error import LegacyError

RemoveVideosFromChannelErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _RemoveVideosFromChannelError:
    def map(self, status_code: int, content: bytes) -> RemoveVideosFromChannelErrorBody:
        match status_code:
            case 403 | 404:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


remove_videos_from_channel_error_mapper: Final[
    ErrorMapper[RemoveVideosFromChannelErrorBody]
] = _RemoveVideosFromChannelError()
