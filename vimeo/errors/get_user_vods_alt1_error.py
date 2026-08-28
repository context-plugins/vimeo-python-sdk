from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

GetUserVodsAlt1ErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _GetUserVodsAlt1Error:
    def map(self, response: HttpResponse) -> GetUserVodsAlt1ErrorBody:
        match response.status_code:
            case 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


get_user_vods_alt1_error_mapper: Final[ErrorMapper[GetUserVodsAlt1ErrorBody]] = _GetUserVodsAlt1Error()
