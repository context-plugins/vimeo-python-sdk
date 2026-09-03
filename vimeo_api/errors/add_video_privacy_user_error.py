from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

AddVideoPrivacyUserErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _AddVideoPrivacyUserError:
    def map(self, response: HttpResponse) -> AddVideoPrivacyUserErrorBody:
        match response.status_code:
            case 403:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


add_video_privacy_user_error_mapper: Final[ErrorMapper[AddVideoPrivacyUserErrorBody]] = _AddVideoPrivacyUserError()
