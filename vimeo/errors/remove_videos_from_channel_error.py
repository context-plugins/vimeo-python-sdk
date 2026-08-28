from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

RemoveVideosFromChannelErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _RemoveVideosFromChannelError:
    def map(self, response: HttpResponse) -> RemoveVideosFromChannelErrorBody:
        match response.status_code:
            case 403 | 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


remove_videos_from_channel_error_mapper: Final[
    ErrorMapper[RemoveVideosFromChannelErrorBody]
] = _RemoveVideosFromChannelError()
