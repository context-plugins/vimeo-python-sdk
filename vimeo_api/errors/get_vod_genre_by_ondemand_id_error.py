from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.legacy_error import LegacyError

GetVodGenreByOndemandIdErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _GetVodGenreByOndemandIdError:
    def map(self, status_code: int, content: bytes) -> GetVodGenreByOndemandIdErrorBody:
        match status_code:
            case 404:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


get_vod_genre_by_ondemand_id_error_mapper: Final[
    ErrorMapper[GetVodGenreByOndemandIdErrorBody]
] = _GetVodGenreByOndemandIdError()
