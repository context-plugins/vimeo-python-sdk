from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

SetVodRegionsErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _SetVodRegionsError:
    def map(self, response: HttpResponse) -> SetVodRegionsErrorBody:
        match response.status_code:
            case 403 | 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


set_vod_regions_error_mapper: Final[ErrorMapper[SetVodRegionsErrorBody]] = _SetVodRegionsError()
