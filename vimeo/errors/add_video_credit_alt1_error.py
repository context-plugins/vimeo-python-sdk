from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

AddVideoCreditAlt1ErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _AddVideoCreditAlt1Error:
    def map(self, response: HttpResponse) -> AddVideoCreditAlt1ErrorBody:
        match response.status_code:
            case 400 | 403:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


add_video_credit_alt1_error_mapper: Final[ErrorMapper[AddVideoCreditAlt1ErrorBody]] = _AddVideoCreditAlt1Error()
