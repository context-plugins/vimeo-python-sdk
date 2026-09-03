from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

CheckIfUserSubscribedToChannelErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _CheckIfUserSubscribedToChannelError:
    def map(self, response: HttpResponse) -> CheckIfUserSubscribedToChannelErrorBody:
        match response.status_code:
            case 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


check_if_user_subscribed_to_channel_error_mapper: Final[
    ErrorMapper[CheckIfUserSubscribedToChannelErrorBody]
] = _CheckIfUserSubscribedToChannelError()
