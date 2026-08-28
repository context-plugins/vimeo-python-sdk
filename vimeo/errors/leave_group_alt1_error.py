from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error
from ..models.legacy_error import LegacyError

LeaveGroupAlt1ErrorBody: TypeAlias = LegacyError | Error | RawError


@dataclass(frozen=True, slots=True)
class _LeaveGroupAlt1Error:
    def map(self, response: HttpResponse) -> LeaveGroupAlt1ErrorBody:
        match response.status_code:
            case 403:
                return decode_json[LegacyError](response)
            case 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


leave_group_alt1_error_mapper: Final[ErrorMapper[LeaveGroupAlt1ErrorBody]] = _LeaveGroupAlt1Error()
