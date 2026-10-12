from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

DeleteOttDestinationErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _DeleteOttDestinationError:
    def map(self, status_code: int, content: bytes) -> DeleteOttDestinationErrorBody:
        match status_code:
            case 400 | 401 | 403 | 404:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


delete_ott_destination_error_mapper: Final[ErrorMapper[DeleteOttDestinationErrorBody]] = _DeleteOttDestinationError()
