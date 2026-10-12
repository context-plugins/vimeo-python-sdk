from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error
from ..models.legacy_error import LegacyError

AddChannelCategoriesErrorBody: TypeAlias = Error | LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _AddChannelCategoriesError:
    def map(self, status_code: int, content: bytes) -> AddChannelCategoriesErrorBody:
        match status_code:
            case 400 | 401 | 403:
                return decode_json[Error](content)
            case 404:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


add_channel_categories_error_mapper: Final[ErrorMapper[AddChannelCategoriesErrorBody]] = _AddChannelCategoriesError()
