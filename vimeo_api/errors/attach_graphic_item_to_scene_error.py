from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

AttachGraphicItemToSceneErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _AttachGraphicItemToSceneError:
    def map(self, response: HttpResponse) -> AttachGraphicItemToSceneErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


attach_graphic_item_to_scene_error_mapper: Final[
    ErrorMapper[AttachGraphicItemToSceneErrorBody]
] = _AttachGraphicItemToSceneError()
