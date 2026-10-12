from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

GetPrivateToMeFolderErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetPrivateToMeFolderError:
    def map(self, status_code: int, content: bytes) -> GetPrivateToMeFolderErrorBody:
        match status_code:
            case 401 | 404:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


get_private_to_me_folder_error_mapper: Final[ErrorMapper[GetPrivateToMeFolderErrorBody]] = _GetPrivateToMeFolderError()
