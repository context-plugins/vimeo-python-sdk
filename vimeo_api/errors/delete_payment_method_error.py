from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

DeletePaymentMethodErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _DeletePaymentMethodError:
    def map(self, response: HttpResponse) -> DeletePaymentMethodErrorBody:
        match response.status_code:
            case 400:
                return decode_json[Error](response)
            case _:
                return RawError(response)


delete_payment_method_error_mapper: Final[ErrorMapper[DeletePaymentMethodErrorBody]] = _DeletePaymentMethodError()
