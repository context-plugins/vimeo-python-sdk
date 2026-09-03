from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error
from ..models.legacy_error import LegacyError

DeleteVideoFromGroupErrorBody: TypeAlias = LegacyError | Error | RawError


@dataclass(frozen=True, slots=True)
class _DeleteVideoFromGroupError:
    def map(self, response: HttpResponse) -> DeleteVideoFromGroupErrorBody:
        match response.status_code:
            case 403:
                return decode_json[LegacyError](response)
            case 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


delete_video_from_group_error_mapper: Final[ErrorMapper[DeleteVideoFromGroupErrorBody]] = _DeleteVideoFromGroupError()
