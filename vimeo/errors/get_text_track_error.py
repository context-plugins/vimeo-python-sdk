from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error
from ..models.legacy_error import LegacyError

GetTextTrackErrorBody: TypeAlias = Error | LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _GetTextTrackError:
    def map(self, response: HttpResponse) -> GetTextTrackErrorBody:
        match response.status_code:
            case 403:
                return decode_json[Error](response)
            case 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


get_text_track_error_mapper: Final[ErrorMapper[GetTextTrackErrorBody]] = _GetTextTrackError()
