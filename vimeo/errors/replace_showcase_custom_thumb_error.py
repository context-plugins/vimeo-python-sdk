from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

ReplaceShowcaseCustomThumbErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _ReplaceShowcaseCustomThumbError:
    def map(self, response: HttpResponse) -> ReplaceShowcaseCustomThumbErrorBody:
        match response.status_code:
            case 403 | 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


replace_showcase_custom_thumb_error_mapper: Final[
    ErrorMapper[ReplaceShowcaseCustomThumbErrorBody]
] = _ReplaceShowcaseCustomThumbError()
