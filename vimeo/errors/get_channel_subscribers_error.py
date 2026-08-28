from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

GetChannelSubscribersErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _GetChannelSubscribersError:
    def map(self, response: HttpResponse) -> GetChannelSubscribersErrorBody:
        match response.status_code:
            case 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


get_channel_subscribers_error_mapper: Final[ErrorMapper[GetChannelSubscribersErrorBody]] = _GetChannelSubscribersError()
