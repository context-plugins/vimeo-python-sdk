from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error
from ..models.legacy_error import LegacyError

CheckIfChannelHasTagErrorBody: TypeAlias = LegacyError | Error | RawError


@dataclass(frozen=True, slots=True)
class _CheckIfChannelHasTagError:
    def map(self, status_code: int, content: bytes) -> CheckIfChannelHasTagErrorBody:
        match status_code:
            case 400:
                return decode_json[LegacyError](content)
            case 404:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


check_if_channel_has_tag_error_mapper: Final[ErrorMapper[CheckIfChannelHasTagErrorBody]] = _CheckIfChannelHasTagError()
