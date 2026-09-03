from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error
from ..models.legacy_error import LegacyError

AddChannelCategoriesErrorBody: TypeAlias = Error | LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _AddChannelCategoriesError:
    def map(self, response: HttpResponse) -> AddChannelCategoriesErrorBody:
        match response.status_code:
            case 400 | 401 | 403:
                return decode_json[Error](response)
            case 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


add_channel_categories_error_mapper: Final[ErrorMapper[AddChannelCategoriesErrorBody]] = _AddChannelCategoriesError()
