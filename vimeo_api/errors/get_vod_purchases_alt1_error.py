from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

GetVodPurchasesAlt1ErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _GetVodPurchasesAlt1Error:
    def map(self, response: HttpResponse) -> GetVodPurchasesAlt1ErrorBody:
        match response.status_code:
            case 403:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


get_vod_purchases_alt1_error_mapper: Final[ErrorMapper[GetVodPurchasesAlt1ErrorBody]] = _GetVodPurchasesAlt1Error()
