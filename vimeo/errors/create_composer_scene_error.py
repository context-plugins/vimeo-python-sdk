from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

CreateComposerSceneErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _CreateComposerSceneError:
    def map(self, response: HttpResponse) -> CreateComposerSceneErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


create_composer_scene_error_mapper: Final[ErrorMapper[CreateComposerSceneErrorBody]] = _CreateComposerSceneError()
