from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

AddVodRegionErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _AddVodRegionError:
    def map(self, response: HttpResponse) -> AddVodRegionErrorBody:
        match response.status_code:
            case 403 | 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


add_vod_region_error_mapper: Final[ErrorMapper[AddVodRegionErrorBody]] = _AddVodRegionError()
