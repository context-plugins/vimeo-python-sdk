from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error
from ..models.legacy_error import LegacyError

CreateAnimatedThumbsetErrorBody: TypeAlias = Error | LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _CreateAnimatedThumbsetError:
    def map(self, response: HttpResponse) -> CreateAnimatedThumbsetErrorBody:
        match response.status_code:
            case 400:
                return decode_json[Error](response)
            case 403 | 429:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


create_animated_thumbset_error_mapper: Final[
    ErrorMapper[CreateAnimatedThumbsetErrorBody]
] = _CreateAnimatedThumbsetError()
