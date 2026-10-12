from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.legacy_error import LegacyError

CopyShowcaseAlt2ErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _CopyShowcaseAlt2Error:
    def map(self, status_code: int, content: bytes) -> CopyShowcaseAlt2ErrorBody:
        match status_code:
            case 403 | 404:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


copy_showcase_alt2_error_mapper: Final[ErrorMapper[CopyShowcaseAlt2ErrorBody]] = _CopyShowcaseAlt2Error()
