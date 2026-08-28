from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error
from ..models.legacy_error import LegacyError

GetChannelsErrorBody: TypeAlias = LegacyError | Error | RawError


@dataclass(frozen=True, slots=True)
class _GetChannelsError:
    def map(self, response: HttpResponse) -> GetChannelsErrorBody:
        match response.status_code:
            case 400:
                return decode_json[LegacyError](response)
            case 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_channels_error_mapper: Final[ErrorMapper[GetChannelsErrorBody]] = _GetChannelsError()
