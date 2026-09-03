from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

AddVodPosterErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _AddVodPosterError:
    def map(self, response: HttpResponse) -> AddVodPosterErrorBody:
        match response.status_code:
            case 403:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


add_vod_poster_error_mapper: Final[ErrorMapper[AddVodPosterErrorBody]] = _AddVodPosterError()
