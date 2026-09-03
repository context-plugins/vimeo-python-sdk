from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

GetShowcaseAlt2ErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _GetShowcaseAlt2Error:
    def map(self, response: HttpResponse) -> GetShowcaseAlt2ErrorBody:
        match response.status_code:
            case 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


get_showcase_alt2_error_mapper: Final[ErrorMapper[GetShowcaseAlt2ErrorBody]] = _GetShowcaseAlt2Error()
