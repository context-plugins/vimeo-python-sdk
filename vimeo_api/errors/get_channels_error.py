from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error
from ..models.legacy_error import LegacyError

GetChannelsErrorBody: TypeAlias = LegacyError | Error | RawError


@dataclass(frozen=True, slots=True)
class _GetChannelsError:
    def map(self, status_code: int, content: bytes) -> GetChannelsErrorBody:
        match status_code:
            case 400:
                return decode_json[LegacyError](content)
            case 404:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


get_channels_error_mapper: Final[ErrorMapper[GetChannelsErrorBody]] = _GetChannelsError()
