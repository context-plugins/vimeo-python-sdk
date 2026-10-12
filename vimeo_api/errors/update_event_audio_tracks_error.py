from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

UpdateEventAudioTracksErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _UpdateEventAudioTracksError:
    def map(self, status_code: int, content: bytes) -> UpdateEventAudioTracksErrorBody:
        match status_code:
            case 401 | 404:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


update_event_audio_tracks_error_mapper: Final[
    ErrorMapper[UpdateEventAudioTracksErrorBody]
] = _UpdateEventAudioTracksError()
