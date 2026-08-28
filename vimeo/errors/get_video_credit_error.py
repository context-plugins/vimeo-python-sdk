from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

GetVideoCreditErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _GetVideoCreditError:
    def map(self, response: HttpResponse) -> GetVideoCreditErrorBody:
        match response.status_code:
            case 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


get_video_credit_error_mapper: Final[ErrorMapper[GetVideoCreditErrorBody]] = _GetVideoCreditError()
