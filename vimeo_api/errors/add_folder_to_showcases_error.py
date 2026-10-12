from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

AddFolderToShowcasesErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _AddFolderToShowcasesError:
    def map(self, status_code: int, content: bytes) -> AddFolderToShowcasesErrorBody:
        match status_code:
            case 400 | 403 | 404:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


add_folder_to_showcases_error_mapper: Final[ErrorMapper[AddFolderToShowcasesErrorBody]] = _AddFolderToShowcasesError()
