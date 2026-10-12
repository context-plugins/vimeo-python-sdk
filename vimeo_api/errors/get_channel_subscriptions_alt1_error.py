from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

GetChannelSubscriptionsAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetChannelSubscriptionsAlt1Error:
    def map(self, status_code: int, content: bytes) -> GetChannelSubscriptionsAlt1ErrorBody:
        match status_code:
            case 404:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


get_channel_subscriptions_alt1_error_mapper: Final[
    ErrorMapper[GetChannelSubscriptionsAlt1ErrorBody]
] = _GetChannelSubscriptionsAlt1Error()
