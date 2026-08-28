from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

SuggestVideoCategoryErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _SuggestVideoCategoryError:
    def map(self, response: HttpResponse) -> SuggestVideoCategoryErrorBody:
        match response.status_code:
            case 403 | 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


suggest_video_category_error_mapper: Final[ErrorMapper[SuggestVideoCategoryErrorBody]] = _SuggestVideoCategoryError()
