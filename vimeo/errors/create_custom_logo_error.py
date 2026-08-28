from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

CreateCustomLogoErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _CreateCustomLogoError:
    def map(self, response: HttpResponse) -> CreateCustomLogoErrorBody:
        match response.status_code:
            case 403:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


create_custom_logo_error_mapper: Final[ErrorMapper[CreateCustomLogoErrorBody]] = _CreateCustomLogoError()
