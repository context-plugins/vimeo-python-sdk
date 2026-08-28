from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

CreateAudioTrackErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _CreateAudioTrackError:
    def map(self, response: HttpResponse) -> CreateAudioTrackErrorBody:
        match response.status_code:
            case 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


create_audio_track_error_mapper: Final[ErrorMapper[CreateAudioTrackErrorBody]] = _CreateAudioTrackError()
