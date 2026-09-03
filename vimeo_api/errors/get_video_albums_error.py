from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetVideoAlbumsErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetVideoAlbumsError:
    def map(self, response: HttpResponse) -> GetVideoAlbumsErrorBody:
        match response.status_code:
            case 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_video_albums_error_mapper: Final[ErrorMapper[GetVideoAlbumsErrorBody]] = _GetVideoAlbumsError()
