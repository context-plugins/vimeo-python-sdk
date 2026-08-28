from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetOttDestinationsErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetOttDestinationsError:
    def map(self, response: HttpResponse) -> GetOttDestinationsErrorBody:
        match response.status_code:
            case 401 | 403 | 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_ott_destinations_error_mapper: Final[ErrorMapper[GetOttDestinationsErrorBody]] = _GetOttDestinationsError()
