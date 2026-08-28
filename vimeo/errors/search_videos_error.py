from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error
from ..models.legacy_error import LegacyError

SearchVideosErrorBody: TypeAlias = Error | LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _SearchVideosError:
    def map(self, response: HttpResponse) -> SearchVideosErrorBody:
        match response.status_code:
            case 400 | 404:
                return decode_json[Error](response)
            case 503:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


search_videos_error_mapper: Final[ErrorMapper[SearchVideosErrorBody]] = _SearchVideosError()
