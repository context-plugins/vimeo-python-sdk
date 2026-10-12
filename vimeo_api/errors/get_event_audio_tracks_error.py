from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

GetEventAudioTracksErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetEventAudioTracksError:
    def map(self, status_code: int, content: bytes) -> GetEventAudioTracksErrorBody:
        match status_code:
            case 401 | 404:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


get_event_audio_tracks_error_mapper: Final[ErrorMapper[GetEventAudioTracksErrorBody]] = _GetEventAudioTracksError()
