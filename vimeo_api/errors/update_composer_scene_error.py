from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

UpdateComposerSceneErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _UpdateComposerSceneError:
    def map(self, status_code: int, content: bytes) -> UpdateComposerSceneErrorBody:
        match status_code:
            case 400 | 401:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


update_composer_scene_error_mapper: Final[ErrorMapper[UpdateComposerSceneErrorBody]] = _UpdateComposerSceneError()
