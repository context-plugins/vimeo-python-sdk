from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetPrivateToMeFolderErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetPrivateToMeFolderError:
    def map(self, response: HttpResponse) -> GetPrivateToMeFolderErrorBody:
        match response.status_code:
            case 401 | 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_private_to_me_folder_error_mapper: Final[ErrorMapper[GetPrivateToMeFolderErrorBody]] = _GetPrivateToMeFolderError()
