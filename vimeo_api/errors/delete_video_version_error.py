from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.legacy_error import LegacyError

DeleteVideoVersionErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _DeleteVideoVersionError:
    def map(self, status_code: int, content: bytes) -> DeleteVideoVersionErrorBody:
        match status_code:
            case 404:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


delete_video_version_error_mapper: Final[ErrorMapper[DeleteVideoVersionErrorBody]] = _DeleteVideoVersionError()
