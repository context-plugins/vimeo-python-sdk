from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetChannelSubscriptionsAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetChannelSubscriptionsAlt1Error:
    def map(self, response: HttpResponse) -> GetChannelSubscriptionsAlt1ErrorBody:
        match response.status_code:
            case 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_channel_subscriptions_alt1_error_mapper: Final[
    ErrorMapper[GetChannelSubscriptionsAlt1ErrorBody]
] = _GetChannelSubscriptionsAlt1Error()
