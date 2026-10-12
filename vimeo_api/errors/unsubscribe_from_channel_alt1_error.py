from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.legacy_error import LegacyError

UnsubscribeFromChannelAlt1ErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _UnsubscribeFromChannelAlt1Error:
    def map(self, status_code: int, content: bytes) -> UnsubscribeFromChannelAlt1ErrorBody:
        match status_code:
            case 404:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


unsubscribe_from_channel_alt1_error_mapper: Final[
    ErrorMapper[UnsubscribeFromChannelAlt1ErrorBody]
] = _UnsubscribeFromChannelAlt1Error()
