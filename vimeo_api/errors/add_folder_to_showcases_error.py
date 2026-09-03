from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

AddFolderToShowcasesErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _AddFolderToShowcasesError:
    def map(self, response: HttpResponse) -> AddFolderToShowcasesErrorBody:
        match response.status_code:
            case 400 | 403 | 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


add_folder_to_showcases_error_mapper: Final[ErrorMapper[AddFolderToShowcasesErrorBody]] = _AddFolderToShowcasesError()
