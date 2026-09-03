from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error
from ..models.legacy_error import LegacyError

CheckIfChannelHasTagErrorBody: TypeAlias = LegacyError | Error | RawError


@dataclass(frozen=True, slots=True)
class _CheckIfChannelHasTagError:
    def map(self, response: HttpResponse) -> CheckIfChannelHasTagErrorBody:
        match response.status_code:
            case 400:
                return decode_json[LegacyError](response)
            case 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


check_if_channel_has_tag_error_mapper: Final[ErrorMapper[CheckIfChannelHasTagErrorBody]] = _CheckIfChannelHasTagError()
