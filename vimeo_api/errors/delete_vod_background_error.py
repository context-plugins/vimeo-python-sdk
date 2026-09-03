from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

DeleteVodBackgroundErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _DeleteVodBackgroundError:
    def map(self, response: HttpResponse) -> DeleteVodBackgroundErrorBody:
        match response.status_code:
            case 403 | 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


delete_vod_background_error_mapper: Final[ErrorMapper[DeleteVodBackgroundErrorBody]] = _DeleteVodBackgroundError()
