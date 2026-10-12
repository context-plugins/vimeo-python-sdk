from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

GetChannelSubscriptionsErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetChannelSubscriptionsError:
    def map(self, status_code: int, content: bytes) -> GetChannelSubscriptionsErrorBody:
        match status_code:
            case 404:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


get_channel_subscriptions_error_mapper: Final[
    ErrorMapper[GetChannelSubscriptionsErrorBody]
] = _GetChannelSubscriptionsError()
