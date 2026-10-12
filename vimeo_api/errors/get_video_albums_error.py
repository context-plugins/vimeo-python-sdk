from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

GetVideoAlbumsErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetVideoAlbumsError:
    def map(self, status_code: int, content: bytes) -> GetVideoAlbumsErrorBody:
        match status_code:
            case 404:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


get_video_albums_error_mapper: Final[ErrorMapper[GetVideoAlbumsErrorBody]] = _GetVideoAlbumsError()
