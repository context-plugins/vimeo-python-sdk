from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

CreateVodPromotionErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _CreateVodPromotionError:
    def map(self, response: HttpResponse) -> CreateVodPromotionErrorBody:
        match response.status_code:
            case 400 | 403 | 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


create_vod_promotion_error_mapper: Final[ErrorMapper[CreateVodPromotionErrorBody]] = _CreateVodPromotionError()
