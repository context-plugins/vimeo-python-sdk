from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

ReplaceShowcaseLogoErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _ReplaceShowcaseLogoError:
    def map(self, response: HttpResponse) -> ReplaceShowcaseLogoErrorBody:
        match response.status_code:
            case 403 | 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


replace_showcase_logo_error_mapper: Final[ErrorMapper[ReplaceShowcaseLogoErrorBody]] = _ReplaceShowcaseLogoError()
