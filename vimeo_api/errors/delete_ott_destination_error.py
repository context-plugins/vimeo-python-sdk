from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

DeleteOttDestinationErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _DeleteOttDestinationError:
    def map(self, response: HttpResponse) -> DeleteOttDestinationErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


delete_ott_destination_error_mapper: Final[ErrorMapper[DeleteOttDestinationErrorBody]] = _DeleteOttDestinationError()
