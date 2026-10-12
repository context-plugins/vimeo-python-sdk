from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.auth_error import AuthError

ConvertAccessTokenErrorBody: TypeAlias = AuthError | RawError


@dataclass(frozen=True, slots=True)
class _ConvertAccessTokenError:
    def map(self, status_code: int, content: bytes) -> ConvertAccessTokenErrorBody:
        match status_code:
            case 400:
                return decode_json[AuthError](content)
            case _:
                return RawError(status_code, content)


convert_access_token_error_mapper: Final[ErrorMapper[ConvertAccessTokenErrorBody]] = _ConvertAccessTokenError()
