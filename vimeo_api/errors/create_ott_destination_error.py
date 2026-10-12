from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

CreateOttDestinationErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _CreateOttDestinationError:
    def map(self, status_code: int, content: bytes) -> CreateOttDestinationErrorBody:
        match status_code:
            case 400 | 401 | 403 | 404:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


create_ott_destination_error_mapper: Final[ErrorMapper[CreateOttDestinationErrorBody]] = _CreateOttDestinationError()
