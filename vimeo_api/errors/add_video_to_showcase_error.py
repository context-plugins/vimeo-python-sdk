from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

AddVideoToShowcaseErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _AddVideoToShowcaseError:
    def map(self, response: HttpResponse) -> AddVideoToShowcaseErrorBody:
        match response.status_code:
            case 403 | 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


add_video_to_showcase_error_mapper: Final[ErrorMapper[AddVideoToShowcaseErrorBody]] = _AddVideoToShowcaseError()
