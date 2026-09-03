from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

CheckIfUserLikedVideoAlt1ErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _CheckIfUserLikedVideoAlt1Error:
    def map(self, response: HttpResponse) -> CheckIfUserLikedVideoAlt1ErrorBody:
        match response.status_code:
            case 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


check_if_user_liked_video_alt1_error_mapper: Final[
    ErrorMapper[CheckIfUserLikedVideoAlt1ErrorBody]
] = _CheckIfUserLikedVideoAlt1Error()
