from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

CheckCategoryForVideoErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _CheckCategoryForVideoError:
    def map(self, response: HttpResponse) -> CheckCategoryForVideoErrorBody:
        match response.status_code:
            case 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


check_category_for_video_error_mapper: Final[
    ErrorMapper[CheckCategoryForVideoErrorBody]
] = _CheckCategoryForVideoError()
