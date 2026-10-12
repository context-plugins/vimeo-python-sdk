from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

GetChannelPrivacyUsersErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetChannelPrivacyUsersError:
    def map(self, status_code: int, content: bytes) -> GetChannelPrivacyUsersErrorBody:
        match status_code:
            case 401 | 403:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


get_channel_privacy_users_error_mapper: Final[
    ErrorMapper[GetChannelPrivacyUsersErrorBody]
] = _GetChannelPrivacyUsersError()
