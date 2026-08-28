from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

DeleteVideoCreditErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _DeleteVideoCreditError:
    def map(self, response: HttpResponse) -> DeleteVideoCreditErrorBody:
        match response.status_code:
            case 400:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


delete_video_credit_error_mapper: Final[ErrorMapper[DeleteVideoCreditErrorBody]] = _DeleteVideoCreditError()
