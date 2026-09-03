from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetAllAnimatedThumbsetErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetAllAnimatedThumbsetError:
    def map(self, response: HttpResponse) -> GetAllAnimatedThumbsetErrorBody:
        match response.status_code:
            case 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_all_animated_thumbset_error_mapper: Final[
    ErrorMapper[GetAllAnimatedThumbsetErrorBody]
] = _GetAllAnimatedThumbsetError()
