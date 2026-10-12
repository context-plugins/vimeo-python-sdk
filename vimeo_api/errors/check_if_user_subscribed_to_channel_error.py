from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.legacy_error import LegacyError

CheckIfUserSubscribedToChannelErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _CheckIfUserSubscribedToChannelError:
    def map(self, status_code: int, content: bytes) -> CheckIfUserSubscribedToChannelErrorBody:
        match status_code:
            case 404:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


check_if_user_subscribed_to_channel_error_mapper: Final[
    ErrorMapper[CheckIfUserSubscribedToChannelErrorBody]
] = _CheckIfUserSubscribedToChannelError()
