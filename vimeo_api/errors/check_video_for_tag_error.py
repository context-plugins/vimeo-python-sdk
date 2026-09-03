from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

CheckVideoForTagErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _CheckVideoForTagError:
    def map(self, response: HttpResponse) -> CheckVideoForTagErrorBody:
        match response.status_code:
            case 400 | 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


check_video_for_tag_error_mapper: Final[ErrorMapper[CheckVideoForTagErrorBody]] = _CheckVideoForTagError()
