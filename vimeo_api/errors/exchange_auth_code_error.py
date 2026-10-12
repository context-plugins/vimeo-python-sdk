from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.auth_error import AuthError

ExchangeAuthCodeErrorBody: TypeAlias = AuthError | RawError


@dataclass(frozen=True, slots=True)
class _ExchangeAuthCodeError:
    def map(self, status_code: int, content: bytes) -> ExchangeAuthCodeErrorBody:
        match status_code:
            case 400:
                return decode_json[AuthError](content)
            case _:
                return RawError(status_code, content)


exchange_auth_code_error_mapper: Final[ErrorMapper[ExchangeAuthCodeErrorBody]] = _ExchangeAuthCodeError()
