from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

RemoveChannelModeratorsErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _RemoveChannelModeratorsError:
    def map(self, response: HttpResponse) -> RemoveChannelModeratorsErrorBody:
        match response.status_code:
            case 403 | 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


remove_channel_moderators_error_mapper: Final[
    ErrorMapper[RemoveChannelModeratorsErrorBody]
] = _RemoveChannelModeratorsError()
