from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

DeleteFolderItemsAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _DeleteFolderItemsAlt1Error:
    def map(self, response: HttpResponse) -> DeleteFolderItemsAlt1ErrorBody:
        match response.status_code:
            case 400 | 401 | 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


delete_folder_items_alt1_error_mapper: Final[
    ErrorMapper[DeleteFolderItemsAlt1ErrorBody]
] = _DeleteFolderItemsAlt1Error()
