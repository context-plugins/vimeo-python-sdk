from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

CreateTextTrackAlt1ErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _CreateTextTrackAlt1Error:
    def map(self, response: HttpResponse) -> CreateTextTrackAlt1ErrorBody:
        match response.status_code:
            case 403:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


create_text_track_alt1_error_mapper: Final[ErrorMapper[CreateTextTrackAlt1ErrorBody]] = _CreateTextTrackAlt1Error()
