from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

EditVideoCreditErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _EditVideoCreditError:
    def map(self, response: HttpResponse) -> EditVideoCreditErrorBody:
        match response.status_code:
            case 400 | 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


edit_video_credit_error_mapper: Final[ErrorMapper[EditVideoCreditErrorBody]] = _EditVideoCreditError()
