from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

GetChapterThumbnailsErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _GetChapterThumbnailsError:
    def map(self, response: HttpResponse) -> GetChapterThumbnailsErrorBody:
        match response.status_code:
            case 403:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


get_chapter_thumbnails_error_mapper: Final[ErrorMapper[GetChapterThumbnailsErrorBody]] = _GetChapterThumbnailsError()
