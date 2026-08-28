from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetAvailableVideoShowcasesErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetAvailableVideoShowcasesError:
    def map(self, response: HttpResponse) -> GetAvailableVideoShowcasesErrorBody:
        match response.status_code:
            case 403:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_available_video_showcases_error_mapper: Final[
    ErrorMapper[GetAvailableVideoShowcasesErrorBody]
] = _GetAvailableVideoShowcasesError()
