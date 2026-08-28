from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

DeleteVideoPrivacyUserErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _DeleteVideoPrivacyUserError:
    def map(self, response: HttpResponse) -> DeleteVideoPrivacyUserErrorBody:
        match response.status_code:
            case 403 | 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


delete_video_privacy_user_error_mapper: Final[
    ErrorMapper[DeleteVideoPrivacyUserErrorBody]
] = _DeleteVideoPrivacyUserError()
