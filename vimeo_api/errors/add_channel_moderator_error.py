from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

AddChannelModeratorErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _AddChannelModeratorError:
    def map(self, response: HttpResponse) -> AddChannelModeratorErrorBody:
        match response.status_code:
            case 403 | 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


add_channel_moderator_error_mapper: Final[ErrorMapper[AddChannelModeratorErrorBody]] = _AddChannelModeratorError()
