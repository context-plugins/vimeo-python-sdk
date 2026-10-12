from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.legacy_error import LegacyError

GetVideoPrivacyDomainsErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _GetVideoPrivacyDomainsError:
    def map(self, status_code: int, content: bytes) -> GetVideoPrivacyDomainsErrorBody:
        match status_code:
            case 403:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


get_video_privacy_domains_error_mapper: Final[
    ErrorMapper[GetVideoPrivacyDomainsErrorBody]
] = _GetVideoPrivacyDomainsError()
