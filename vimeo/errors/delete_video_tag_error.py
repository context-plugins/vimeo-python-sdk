from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

DeleteVideoTagErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _DeleteVideoTagError:
    def map(self, response: HttpResponse) -> DeleteVideoTagErrorBody:
        match response.status_code:
            case 400:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


delete_video_tag_error_mapper: Final[ErrorMapper[DeleteVideoTagErrorBody]] = _DeleteVideoTagError()
