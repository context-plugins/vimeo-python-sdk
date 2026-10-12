from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.legacy_error import LegacyError

CreateChapterThumbnailOrUploadLinkErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _CreateChapterThumbnailOrUploadLinkError:
    def map(self, status_code: int, content: bytes) -> CreateChapterThumbnailOrUploadLinkErrorBody:
        match status_code:
            case 403:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


create_chapter_thumbnail_or_upload_link_error_mapper: Final[
    ErrorMapper[CreateChapterThumbnailOrUploadLinkErrorBody]
] = _CreateChapterThumbnailOrUploadLinkError()
