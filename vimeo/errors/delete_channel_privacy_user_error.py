from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

DeleteChannelPrivacyUserErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _DeleteChannelPrivacyUserError:
    def map(self, response: HttpResponse) -> DeleteChannelPrivacyUserErrorBody:
        match response.status_code:
            case 401 | 403:
                return decode_json[Error](response)
            case _:
                return RawError(response)


delete_channel_privacy_user_error_mapper: Final[
    ErrorMapper[DeleteChannelPrivacyUserErrorBody]
] = _DeleteChannelPrivacyUserError()
