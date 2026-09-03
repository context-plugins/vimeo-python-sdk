from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

GetVodGenreByOndemandIdErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _GetVodGenreByOndemandIdError:
    def map(self, response: HttpResponse) -> GetVodGenreByOndemandIdErrorBody:
        match response.status_code:
            case 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


get_vod_genre_by_ondemand_id_error_mapper: Final[
    ErrorMapper[GetVodGenreByOndemandIdErrorBody]
] = _GetVodGenreByOndemandIdError()
