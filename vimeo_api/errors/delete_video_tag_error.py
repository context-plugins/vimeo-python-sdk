from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.legacy_error import LegacyError

DeleteVideoTagErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _DeleteVideoTagError:
    def map(self, status_code: int, content: bytes) -> DeleteVideoTagErrorBody:
        match status_code:
            case 400:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


delete_video_tag_error_mapper: Final[ErrorMapper[DeleteVideoTagErrorBody]] = _DeleteVideoTagError()
