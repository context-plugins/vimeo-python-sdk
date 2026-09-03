from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error
from ..models.legacy_error import LegacyError

GetVideoVersionsErrorBody: TypeAlias = Error | LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _GetVideoVersionsError:
    def map(self, response: HttpResponse) -> GetVideoVersionsErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Error](response)
            case 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


get_video_versions_error_mapper: Final[ErrorMapper[GetVideoVersionsErrorBody]] = _GetVideoVersionsError()
