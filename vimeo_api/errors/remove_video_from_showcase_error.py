from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

RemoveVideoFromShowcaseErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _RemoveVideoFromShowcaseError:
    def map(self, response: HttpResponse) -> RemoveVideoFromShowcaseErrorBody:
        match response.status_code:
            case 403 | 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


remove_video_from_showcase_error_mapper: Final[
    ErrorMapper[RemoveVideoFromShowcaseErrorBody]
] = _RemoveVideoFromShowcaseError()
