from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

ReplaceVideosInShowcaseAlt2ErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _ReplaceVideosInShowcaseAlt2Error:
    def map(self, response: HttpResponse) -> ReplaceVideosInShowcaseAlt2ErrorBody:
        match response.status_code:
            case 403 | 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


replace_videos_in_showcase_alt2_error_mapper: Final[
    ErrorMapper[ReplaceVideosInShowcaseAlt2ErrorBody]
] = _ReplaceVideosInShowcaseAlt2Error()
