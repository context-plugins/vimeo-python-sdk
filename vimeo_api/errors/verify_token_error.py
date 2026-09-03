from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

VerifyTokenErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _VerifyTokenError:
    def map(self, response: HttpResponse) -> VerifyTokenErrorBody:
        match response.status_code:
            case 401:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


verify_token_error_mapper: Final[ErrorMapper[VerifyTokenErrorBody]] = _VerifyTokenError()
