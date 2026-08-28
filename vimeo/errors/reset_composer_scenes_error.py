from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

ResetComposerScenesErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _ResetComposerScenesError:
    def map(self, response: HttpResponse) -> ResetComposerScenesErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


reset_composer_scenes_error_mapper: Final[ErrorMapper[ResetComposerScenesErrorBody]] = _ResetComposerScenesError()
