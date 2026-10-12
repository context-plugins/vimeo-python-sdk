from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

GetPaymentMethodInfoErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetPaymentMethodInfoError:
    def map(self, status_code: int, content: bytes) -> GetPaymentMethodInfoErrorBody:
        match status_code:
            case 404:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


get_payment_method_info_error_mapper: Final[ErrorMapper[GetPaymentMethodInfoErrorBody]] = _GetPaymentMethodInfoError()
