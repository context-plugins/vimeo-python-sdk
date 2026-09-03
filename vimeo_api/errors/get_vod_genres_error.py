from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetVodGenresErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetVodGenresError:
    def map(self, response: HttpResponse) -> GetVodGenresErrorBody:
        match response.status_code:
            case 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_vod_genres_error_mapper: Final[ErrorMapper[GetVodGenresErrorBody]] = _GetVodGenresError()
