from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

GetVodPromotionCodesErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _GetVodPromotionCodesError:
    def map(self, response: HttpResponse) -> GetVodPromotionCodesErrorBody:
        match response.status_code:
            case 403 | 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


get_vod_promotion_codes_error_mapper: Final[ErrorMapper[GetVodPromotionCodesErrorBody]] = _GetVodPromotionCodesError()
