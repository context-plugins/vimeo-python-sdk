from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

DeleteShowcaseAlt2ErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _DeleteShowcaseAlt2Error:
    def map(self, response: HttpResponse) -> DeleteShowcaseAlt2ErrorBody:
        match response.status_code:
            case 403 | 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


delete_showcase_alt2_error_mapper: Final[ErrorMapper[DeleteShowcaseAlt2ErrorBody]] = _DeleteShowcaseAlt2Error()
