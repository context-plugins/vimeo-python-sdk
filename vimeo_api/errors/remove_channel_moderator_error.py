from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

RemoveChannelModeratorErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _RemoveChannelModeratorError:
    def map(self, response: HttpResponse) -> RemoveChannelModeratorErrorBody:
        match response.status_code:
            case 403 | 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


remove_channel_moderator_error_mapper: Final[
    ErrorMapper[RemoveChannelModeratorErrorBody]
] = _RemoveChannelModeratorError()
