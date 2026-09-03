from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetPaymentMethodInfoErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetPaymentMethodInfoError:
    def map(self, response: HttpResponse) -> GetPaymentMethodInfoErrorBody:
        match response.status_code:
            case 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_payment_method_info_error_mapper: Final[ErrorMapper[GetPaymentMethodInfoErrorBody]] = _GetPaymentMethodInfoError()
