from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.legacy_error import LegacyError

GetVideoPrivacyUsersAlt1ErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _GetVideoPrivacyUsersAlt1Error:
    def map(self, status_code: int, content: bytes) -> GetVideoPrivacyUsersAlt1ErrorBody:
        match status_code:
            case 400:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


get_video_privacy_users_alt1_error_mapper: Final[
    ErrorMapper[GetVideoPrivacyUsersAlt1ErrorBody]
] = _GetVideoPrivacyUsersAlt1Error()
