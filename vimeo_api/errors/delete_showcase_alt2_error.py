from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.legacy_error import LegacyError

DeleteShowcaseAlt2ErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _DeleteShowcaseAlt2Error:
    def map(self, status_code: int, content: bytes) -> DeleteShowcaseAlt2ErrorBody:
        match status_code:
            case 403 | 404:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


delete_showcase_alt2_error_mapper: Final[ErrorMapper[DeleteShowcaseAlt2ErrorBody]] = _DeleteShowcaseAlt2Error()
