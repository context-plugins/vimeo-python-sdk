from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

SetChannelPrivacyUserErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _SetChannelPrivacyUserError:
    def map(self, status_code: int, content: bytes) -> SetChannelPrivacyUserErrorBody:
        match status_code:
            case 401 | 403:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


set_channel_privacy_user_error_mapper: Final[
    ErrorMapper[SetChannelPrivacyUserErrorBody]
] = _SetChannelPrivacyUserError()
