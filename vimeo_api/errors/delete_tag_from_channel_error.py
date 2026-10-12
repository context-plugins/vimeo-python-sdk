from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error
from ..models.legacy_error import LegacyError

DeleteTagFromChannelErrorBody: TypeAlias = LegacyError | Error | RawError


@dataclass(frozen=True, slots=True)
class _DeleteTagFromChannelError:
    def map(self, status_code: int, content: bytes) -> DeleteTagFromChannelErrorBody:
        match status_code:
            case 400:
                return decode_json[LegacyError](content)
            case 401 | 403:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


delete_tag_from_channel_error_mapper: Final[ErrorMapper[DeleteTagFromChannelErrorBody]] = _DeleteTagFromChannelError()
