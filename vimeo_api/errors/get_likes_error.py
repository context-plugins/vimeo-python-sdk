from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetLikesErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetLikesError:
    def map(self, response: HttpResponse) -> GetLikesErrorBody:
        match response.status_code:
            case 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_likes_error_mapper: Final[ErrorMapper[GetLikesErrorBody]] = _GetLikesError()
