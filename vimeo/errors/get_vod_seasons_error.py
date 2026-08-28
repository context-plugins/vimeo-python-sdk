from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

GetVodSeasonsErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _GetVodSeasonsError:
    def map(self, response: HttpResponse) -> GetVodSeasonsErrorBody:
        match response.status_code:
            case 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


get_vod_seasons_error_mapper: Final[ErrorMapper[GetVodSeasonsErrorBody]] = _GetVodSeasonsError()
