from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error
from ..models.legacy_error import LegacyError

AddChannelTagErrorBody: TypeAlias = LegacyError | Error | RawError


@dataclass(frozen=True, slots=True)
class _AddChannelTagError:
    def map(self, status_code: int, content: bytes) -> AddChannelTagErrorBody:
        match status_code:
            case 400:
                return decode_json[LegacyError](content)
            case 401 | 403:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


add_channel_tag_error_mapper: Final[ErrorMapper[AddChannelTagErrorBody]] = _AddChannelTagError()
