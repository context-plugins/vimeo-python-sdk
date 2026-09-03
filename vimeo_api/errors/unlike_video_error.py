from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

UnlikeVideoErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _UnlikeVideoError:
    def map(self, response: HttpResponse) -> UnlikeVideoErrorBody:
        match response.status_code:
            case 403:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


unlike_video_error_mapper: Final[ErrorMapper[UnlikeVideoErrorBody]] = _UnlikeVideoError()
