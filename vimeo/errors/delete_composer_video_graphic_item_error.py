from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

DeleteComposerVideoGraphicItemErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _DeleteComposerVideoGraphicItemError:
    def map(self, response: HttpResponse) -> DeleteComposerVideoGraphicItemErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


delete_composer_video_graphic_item_error_mapper: Final[
    ErrorMapper[DeleteComposerVideoGraphicItemErrorBody]
] = _DeleteComposerVideoGraphicItemError()
