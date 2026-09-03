from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

AddComposerVideoGraphicItemErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _AddComposerVideoGraphicItemError:
    def map(self, response: HttpResponse) -> AddComposerVideoGraphicItemErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


add_composer_video_graphic_item_error_mapper: Final[
    ErrorMapper[AddComposerVideoGraphicItemErrorBody]
] = _AddComposerVideoGraphicItemError()
