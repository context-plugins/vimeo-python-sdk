from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

DeleteVideoErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _DeleteVideoError:
    def map(self, response: HttpResponse) -> DeleteVideoErrorBody:
        match response.status_code:
            case 403:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


delete_video_error_mapper: Final[ErrorMapper[DeleteVideoErrorBody]] = _DeleteVideoError()
