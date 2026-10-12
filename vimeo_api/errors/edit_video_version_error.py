from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error
from ..models.legacy_error import LegacyError

EditVideoVersionErrorBody: TypeAlias = Error | LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _EditVideoVersionError:
    def map(self, status_code: int, content: bytes) -> EditVideoVersionErrorBody:
        match status_code:
            case 401:
                return decode_json[Error](content)
            case 404:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


edit_video_version_error_mapper: Final[ErrorMapper[EditVideoVersionErrorBody]] = _EditVideoVersionError()
