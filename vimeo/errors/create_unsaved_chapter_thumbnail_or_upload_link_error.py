from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

CreateUnsavedChapterThumbnailOrUploadLinkErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _CreateUnsavedChapterThumbnailOrUploadLinkError:
    def map(self, response: HttpResponse) -> CreateUnsavedChapterThumbnailOrUploadLinkErrorBody:
        match response.status_code:
            case 403:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


create_unsaved_chapter_thumbnail_or_upload_link_error_mapper: Final[
    ErrorMapper[CreateUnsavedChapterThumbnailOrUploadLinkErrorBody]
] = _CreateUnsavedChapterThumbnailOrUploadLinkError()
