from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

GetVideoPrivacyDomainsErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _GetVideoPrivacyDomainsError:
    def map(self, response: HttpResponse) -> GetVideoPrivacyDomainsErrorBody:
        match response.status_code:
            case 403:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


get_video_privacy_domains_error_mapper: Final[
    ErrorMapper[GetVideoPrivacyDomainsErrorBody]
] = _GetVideoPrivacyDomainsError()
