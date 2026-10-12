from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error
from ..models.legacy_error import LegacyError

AddChannelModeratorsErrorBody: TypeAlias = Error | LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _AddChannelModeratorsError:
    def map(self, status_code: int, content: bytes) -> AddChannelModeratorsErrorBody:
        match status_code:
            case 400:
                return decode_json[Error](content)
            case 403 | 404:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


add_channel_moderators_error_mapper: Final[ErrorMapper[AddChannelModeratorsErrorBody]] = _AddChannelModeratorsError()
