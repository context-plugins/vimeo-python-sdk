from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

UnsubscribeFromChannelAlt1ErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _UnsubscribeFromChannelAlt1Error:
    def map(self, response: HttpResponse) -> UnsubscribeFromChannelAlt1ErrorBody:
        match response.status_code:
            case 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


unsubscribe_from_channel_alt1_error_mapper: Final[
    ErrorMapper[UnsubscribeFromChannelAlt1ErrorBody]
] = _UnsubscribeFromChannelAlt1Error()
