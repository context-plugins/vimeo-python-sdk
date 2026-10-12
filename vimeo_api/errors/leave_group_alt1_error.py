from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error
from ..models.legacy_error import LegacyError

LeaveGroupAlt1ErrorBody: TypeAlias = LegacyError | Error | RawError


@dataclass(frozen=True, slots=True)
class _LeaveGroupAlt1Error:
    def map(self, status_code: int, content: bytes) -> LeaveGroupAlt1ErrorBody:
        match status_code:
            case 403:
                return decode_json[LegacyError](content)
            case 404:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


leave_group_alt1_error_mapper: Final[ErrorMapper[LeaveGroupAlt1ErrorBody]] = _LeaveGroupAlt1Error()
