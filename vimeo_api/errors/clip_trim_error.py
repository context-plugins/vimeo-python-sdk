from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

ClipTrimErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _ClipTrimError:
    def map(self, response: HttpResponse) -> ClipTrimErrorBody:
        match response.status_code:
            case 401 | 403:
                return decode_json[Error](response)
            case _:
                return RawError(response)


clip_trim_error_mapper: Final[ErrorMapper[ClipTrimErrorBody]] = _ClipTrimError()
