from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

GetCategoryVideosErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _GetCategoryVideosError:
    def map(self, response: HttpResponse) -> GetCategoryVideosErrorBody:
        match response.status_code:
            case 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


get_category_videos_error_mapper: Final[ErrorMapper[GetCategoryVideosErrorBody]] = _GetCategoryVideosError()
