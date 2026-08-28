from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetChannelSubscriptionsErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetChannelSubscriptionsError:
    def map(self, response: HttpResponse) -> GetChannelSubscriptionsErrorBody:
        match response.status_code:
            case 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_channel_subscriptions_error_mapper: Final[
    ErrorMapper[GetChannelSubscriptionsErrorBody]
] = _GetChannelSubscriptionsError()
