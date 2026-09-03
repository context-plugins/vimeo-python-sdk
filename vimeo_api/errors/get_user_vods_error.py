from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

GetUserVodsErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _GetUserVodsError:
    def map(self, response: HttpResponse) -> GetUserVodsErrorBody:
        match response.status_code:
            case 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


get_user_vods_error_mapper: Final[ErrorMapper[GetUserVodsErrorBody]] = _GetUserVodsError()
