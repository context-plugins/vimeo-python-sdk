from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

CreateShowcaseCustomThumbErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _CreateShowcaseCustomThumbError:
    def map(self, response: HttpResponse) -> CreateShowcaseCustomThumbErrorBody:
        match response.status_code:
            case 403 | 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


create_showcase_custom_thumb_error_mapper: Final[
    ErrorMapper[CreateShowcaseCustomThumbErrorBody]
] = _CreateShowcaseCustomThumbError()
