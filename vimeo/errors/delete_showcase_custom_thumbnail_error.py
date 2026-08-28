from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

DeleteShowcaseCustomThumbnailErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _DeleteShowcaseCustomThumbnailError:
    def map(self, response: HttpResponse) -> DeleteShowcaseCustomThumbnailErrorBody:
        match response.status_code:
            case 403 | 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


delete_showcase_custom_thumbnail_error_mapper: Final[
    ErrorMapper[DeleteShowcaseCustomThumbnailErrorBody]
] = _DeleteShowcaseCustomThumbnailError()
