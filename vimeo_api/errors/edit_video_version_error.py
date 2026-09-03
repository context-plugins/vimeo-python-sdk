from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error
from ..models.legacy_error import LegacyError

EditVideoVersionErrorBody: TypeAlias = Error | LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _EditVideoVersionError:
    def map(self, response: HttpResponse) -> EditVideoVersionErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Error](response)
            case 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


edit_video_version_error_mapper: Final[ErrorMapper[EditVideoVersionErrorBody]] = _EditVideoVersionError()
