from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.legacy_error import LegacyError

SubscribeToChannelAlt1ErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _SubscribeToChannelAlt1Error:
    def map(self, status_code: int, content: bytes) -> SubscribeToChannelAlt1ErrorBody:
        match status_code:
            case 404:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


subscribe_to_channel_alt1_error_mapper: Final[
    ErrorMapper[SubscribeToChannelAlt1ErrorBody]
] = _SubscribeToChannelAlt1Error()
