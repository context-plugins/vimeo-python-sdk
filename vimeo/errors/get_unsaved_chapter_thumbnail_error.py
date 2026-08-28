from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

GetUnsavedChapterThumbnailErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _GetUnsavedChapterThumbnailError:
    def map(self, response: HttpResponse) -> GetUnsavedChapterThumbnailErrorBody:
        match response.status_code:
            case 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


get_unsaved_chapter_thumbnail_error_mapper: Final[
    ErrorMapper[GetUnsavedChapterThumbnailErrorBody]
] = _GetUnsavedChapterThumbnailError()
