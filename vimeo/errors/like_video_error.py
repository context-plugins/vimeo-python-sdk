from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

LikeVideoErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _LikeVideoError:
    def map(self, response: HttpResponse) -> LikeVideoErrorBody:
        match response.status_code:
            case 400 | 403:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


like_video_error_mapper: Final[ErrorMapper[LikeVideoErrorBody]] = _LikeVideoError()
