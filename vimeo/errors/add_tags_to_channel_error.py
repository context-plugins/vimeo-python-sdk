from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error
from ..models.legacy_error import LegacyError

AddTagsToChannelErrorBody: TypeAlias = LegacyError | Error | RawError


@dataclass(frozen=True, slots=True)
class _AddTagsToChannelError:
    def map(self, response: HttpResponse) -> AddTagsToChannelErrorBody:
        match response.status_code:
            case 400:
                return decode_json[LegacyError](response)
            case 401 | 403:
                return decode_json[Error](response)
            case _:
                return RawError(response)


add_tags_to_channel_error_mapper: Final[ErrorMapper[AddTagsToChannelErrorBody]] = _AddTagsToChannelError()
