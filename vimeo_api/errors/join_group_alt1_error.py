from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error
from ..models.legacy_error import LegacyError

JoinGroupAlt1ErrorBody: TypeAlias = LegacyError | Error | RawError


@dataclass(frozen=True, slots=True)
class _JoinGroupAlt1Error:
    def map(self, response: HttpResponse) -> JoinGroupAlt1ErrorBody:
        match response.status_code:
            case 403:
                return decode_json[LegacyError](response)
            case 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


join_group_alt1_error_mapper: Final[ErrorMapper[JoinGroupAlt1ErrorBody]] = _JoinGroupAlt1Error()
