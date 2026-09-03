from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

CreateVideoVersionErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _CreateVideoVersionError:
    def map(self, response: HttpResponse) -> CreateVideoVersionErrorBody:
        match response.status_code:
            case 400 | 403 | 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


create_video_version_error_mapper: Final[ErrorMapper[CreateVideoVersionErrorBody]] = _CreateVideoVersionError()
