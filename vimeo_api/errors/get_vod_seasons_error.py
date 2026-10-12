from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.legacy_error import LegacyError

GetVodSeasonsErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _GetVodSeasonsError:
    def map(self, status_code: int, content: bytes) -> GetVodSeasonsErrorBody:
        match status_code:
            case 404:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


get_vod_seasons_error_mapper: Final[ErrorMapper[GetVodSeasonsErrorBody]] = _GetVodSeasonsError()
