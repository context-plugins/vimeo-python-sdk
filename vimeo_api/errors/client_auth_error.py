from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

ClientAuthErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _ClientAuthError:
    def map(self, response: HttpResponse) -> ClientAuthErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


client_auth_error_mapper: Final[ErrorMapper[ClientAuthErrorBody]] = _ClientAuthError()
