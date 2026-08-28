from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

CreateShowcaseErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _CreateShowcaseError:
    def map(self, response: HttpResponse) -> CreateShowcaseErrorBody:
        match response.status_code:
            case 400 | 403:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


create_showcase_error_mapper: Final[ErrorMapper[CreateShowcaseErrorBody]] = _CreateShowcaseError()
