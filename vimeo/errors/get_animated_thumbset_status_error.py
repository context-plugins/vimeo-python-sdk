from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetAnimatedThumbsetStatusErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetAnimatedThumbsetStatusError:
    def map(self, response: HttpResponse) -> GetAnimatedThumbsetStatusErrorBody:
        match response.status_code:
            case 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_animated_thumbset_status_error_mapper: Final[
    ErrorMapper[GetAnimatedThumbsetStatusErrorBody]
] = _GetAnimatedThumbsetStatusError()
