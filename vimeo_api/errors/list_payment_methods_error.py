from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

ListPaymentMethodsErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _ListPaymentMethodsError:
    def map(self, response: HttpResponse) -> ListPaymentMethodsErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


list_payment_methods_error_mapper: Final[ErrorMapper[ListPaymentMethodsErrorBody]] = _ListPaymentMethodsError()
