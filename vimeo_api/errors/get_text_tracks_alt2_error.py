from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

GetTextTracksAlt2ErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _GetTextTracksAlt2Error:
    def map(self, response: HttpResponse) -> GetTextTracksAlt2ErrorBody:
        match response.status_code:
            case 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


get_text_tracks_alt2_error_mapper: Final[ErrorMapper[GetTextTracksAlt2ErrorBody]] = _GetTextTracksAlt2Error()
