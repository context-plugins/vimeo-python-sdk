from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

CreateVideoCustomLogoErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _CreateVideoCustomLogoError:
    def map(self, response: HttpResponse) -> CreateVideoCustomLogoErrorBody:
        match response.status_code:
            case 403 | 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


create_video_custom_logo_error_mapper: Final[
    ErrorMapper[CreateVideoCustomLogoErrorBody]
] = _CreateVideoCustomLogoError()
