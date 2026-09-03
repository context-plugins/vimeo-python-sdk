from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

DeleteAudioTrackErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _DeleteAudioTrackError:
    def map(self, response: HttpResponse) -> DeleteAudioTrackErrorBody:
        match response.status_code:
            case 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


delete_audio_track_error_mapper: Final[ErrorMapper[DeleteAudioTrackErrorBody]] = _DeleteAudioTrackError()
