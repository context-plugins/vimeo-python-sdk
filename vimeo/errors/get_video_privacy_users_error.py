from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

GetVideoPrivacyUsersErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _GetVideoPrivacyUsersError:
    def map(self, response: HttpResponse) -> GetVideoPrivacyUsersErrorBody:
        match response.status_code:
            case 400:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


get_video_privacy_users_error_mapper: Final[ErrorMapper[GetVideoPrivacyUsersErrorBody]] = _GetVideoPrivacyUsersError()
