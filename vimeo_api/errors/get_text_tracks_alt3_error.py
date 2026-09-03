from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

GetTextTracksAlt3ErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _GetTextTracksAlt3Error:
    def map(self, response: HttpResponse) -> GetTextTracksAlt3ErrorBody:
        match response.status_code:
            case 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


get_text_tracks_alt3_error_mapper: Final[ErrorMapper[GetTextTracksAlt3ErrorBody]] = _GetTextTracksAlt3Error()
