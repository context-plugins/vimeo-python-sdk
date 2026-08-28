from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

SetChannelPrivacyUserErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _SetChannelPrivacyUserError:
    def map(self, response: HttpResponse) -> SetChannelPrivacyUserErrorBody:
        match response.status_code:
            case 401 | 403:
                return decode_json[Error](response)
            case _:
                return RawError(response)


set_channel_privacy_user_error_mapper: Final[
    ErrorMapper[SetChannelPrivacyUserErrorBody]
] = _SetChannelPrivacyUserError()
