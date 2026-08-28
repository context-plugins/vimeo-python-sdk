from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

AddVideoTagsErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _AddVideoTagsError:
    def map(self, response: HttpResponse) -> AddVideoTagsErrorBody:
        match response.status_code:
            case 400 | 403:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


add_video_tags_error_mapper: Final[ErrorMapper[AddVideoTagsErrorBody]] = _AddVideoTagsError()
