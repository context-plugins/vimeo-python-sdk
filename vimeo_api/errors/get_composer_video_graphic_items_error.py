from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

GetComposerVideoGraphicItemsErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetComposerVideoGraphicItemsError:
    def map(self, status_code: int, content: bytes) -> GetComposerVideoGraphicItemsErrorBody:
        match status_code:
            case 400 | 401:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


get_composer_video_graphic_items_error_mapper: Final[
    ErrorMapper[GetComposerVideoGraphicItemsErrorBody]
] = _GetComposerVideoGraphicItemsError()
