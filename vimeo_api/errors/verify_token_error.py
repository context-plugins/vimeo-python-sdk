from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.legacy_error import LegacyError

VerifyTokenErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _VerifyTokenError:
    def map(self, status_code: int, content: bytes) -> VerifyTokenErrorBody:
        match status_code:
            case 401:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


verify_token_error_mapper: Final[ErrorMapper[VerifyTokenErrorBody]] = _VerifyTokenError()
