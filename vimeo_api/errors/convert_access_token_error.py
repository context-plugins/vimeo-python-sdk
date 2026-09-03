from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.auth_error import AuthError

ConvertAccessTokenErrorBody: TypeAlias = AuthError | RawError


@dataclass(frozen=True, slots=True)
class _ConvertAccessTokenError:
    def map(self, response: HttpResponse) -> ConvertAccessTokenErrorBody:
        match response.status_code:
            case 400:
                return decode_json[AuthError](response)
            case _:
                return RawError(response)


convert_access_token_error_mapper: Final[ErrorMapper[ConvertAccessTokenErrorBody]] = _ConvertAccessTokenError()
