from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetEventAudioTracksErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetEventAudioTracksError:
    def map(self, response: HttpResponse) -> GetEventAudioTracksErrorBody:
        match response.status_code:
            case 401 | 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_event_audio_tracks_error_mapper: Final[ErrorMapper[GetEventAudioTracksErrorBody]] = _GetEventAudioTracksError()
