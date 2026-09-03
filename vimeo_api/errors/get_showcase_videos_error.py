from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

GetShowcaseVideosErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _GetShowcaseVideosError:
    def map(self, response: HttpResponse) -> GetShowcaseVideosErrorBody:
        match response.status_code:
            case 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


get_showcase_videos_error_mapper: Final[ErrorMapper[GetShowcaseVideosErrorBody]] = _GetShowcaseVideosError()
