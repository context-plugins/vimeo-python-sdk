from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

CheckIfVodWasPurchasedAlt1ErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _CheckIfVodWasPurchasedAlt1Error:
    def map(self, response: HttpResponse) -> CheckIfVodWasPurchasedAlt1ErrorBody:
        match response.status_code:
            case 403 | 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


check_if_vod_was_purchased_alt1_error_mapper: Final[
    ErrorMapper[CheckIfVodWasPurchasedAlt1ErrorBody]
] = _CheckIfVodWasPurchasedAlt1Error()
