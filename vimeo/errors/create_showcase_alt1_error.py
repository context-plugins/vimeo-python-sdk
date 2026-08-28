from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

CreateShowcaseAlt1ErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _CreateShowcaseAlt1Error:
    def map(self, response: HttpResponse) -> CreateShowcaseAlt1ErrorBody:
        match response.status_code:
            case 400 | 403:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


create_showcase_alt1_error_mapper: Final[ErrorMapper[CreateShowcaseAlt1ErrorBody]] = _CreateShowcaseAlt1Error()
