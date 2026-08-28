from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

DeleteVodRegionsErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _DeleteVodRegionsError:
    def map(self, response: HttpResponse) -> DeleteVodRegionsErrorBody:
        match response.status_code:
            case 403 | 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


delete_vod_regions_error_mapper: Final[ErrorMapper[DeleteVodRegionsErrorBody]] = _DeleteVodRegionsError()
