from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

EditUserErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _EditUserError:
    def map(self, response: HttpResponse) -> EditUserErrorBody:
        match response.status_code:
            case 400:
                return decode_json[Error](response)
            case _:
                return RawError(response)


edit_user_error_mapper: Final[ErrorMapper[EditUserErrorBody]] = _EditUserError()
