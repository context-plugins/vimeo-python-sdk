from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

DeleteLiveEventDestinationErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _DeleteLiveEventDestinationError:
    def map(self, status_code: int, content: bytes) -> DeleteLiveEventDestinationErrorBody:
        match status_code:
            case 401 | 403 | 404:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


delete_live_event_destination_error_mapper: Final[
    ErrorMapper[DeleteLiveEventDestinationErrorBody]
] = _DeleteLiveEventDestinationError()
