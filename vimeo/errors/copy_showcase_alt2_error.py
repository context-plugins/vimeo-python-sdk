from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

CopyShowcaseAlt2ErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _CopyShowcaseAlt2Error:
    def map(self, response: HttpResponse) -> CopyShowcaseAlt2ErrorBody:
        match response.status_code:
            case 403 | 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


copy_showcase_alt2_error_mapper: Final[ErrorMapper[CopyShowcaseAlt2ErrorBody]] = _CopyShowcaseAlt2Error()
