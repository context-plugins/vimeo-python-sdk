from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

GetVideoPrivacyUsersAlt1ErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _GetVideoPrivacyUsersAlt1Error:
    def map(self, response: HttpResponse) -> GetVideoPrivacyUsersAlt1ErrorBody:
        match response.status_code:
            case 400:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


get_video_privacy_users_alt1_error_mapper: Final[
    ErrorMapper[GetVideoPrivacyUsersAlt1ErrorBody]
] = _GetVideoPrivacyUsersAlt1Error()
