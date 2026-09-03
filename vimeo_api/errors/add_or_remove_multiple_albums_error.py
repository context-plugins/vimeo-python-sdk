from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

AddOrRemoveMultipleAlbumsErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _AddOrRemoveMultipleAlbumsError:
    def map(self, response: HttpResponse) -> AddOrRemoveMultipleAlbumsErrorBody:
        match response.status_code:
            case 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


add_or_remove_multiple_albums_error_mapper: Final[
    ErrorMapper[AddOrRemoveMultipleAlbumsErrorBody]
] = _AddOrRemoveMultipleAlbumsError()
