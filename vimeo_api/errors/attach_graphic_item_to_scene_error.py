from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

AttachGraphicItemToSceneErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _AttachGraphicItemToSceneError:
    def map(self, status_code: int, content: bytes) -> AttachGraphicItemToSceneErrorBody:
        match status_code:
            case 400 | 401:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


attach_graphic_item_to_scene_error_mapper: Final[
    ErrorMapper[AttachGraphicItemToSceneErrorBody]
] = _AttachGraphicItemToSceneError()
