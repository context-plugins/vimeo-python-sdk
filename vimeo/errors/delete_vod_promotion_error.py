from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

DeleteVodPromotionErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _DeleteVodPromotionError:
    def map(self, response: HttpResponse) -> DeleteVodPromotionErrorBody:
        match response.status_code:
            case 403 | 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


delete_vod_promotion_error_mapper: Final[ErrorMapper[DeleteVodPromotionErrorBody]] = _DeleteVodPromotionError()
