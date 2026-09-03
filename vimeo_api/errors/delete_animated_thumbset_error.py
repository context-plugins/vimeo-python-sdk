from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

DeleteAnimatedThumbsetErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _DeleteAnimatedThumbsetError:
    def map(self, response: HttpResponse) -> DeleteAnimatedThumbsetErrorBody:
        match response.status_code:
            case 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


delete_animated_thumbset_error_mapper: Final[
    ErrorMapper[DeleteAnimatedThumbsetErrorBody]
] = _DeleteAnimatedThumbsetError()
