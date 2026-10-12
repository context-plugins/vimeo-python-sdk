from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

GetCategorySubscriptionsErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetCategorySubscriptionsError:
    def map(self, status_code: int, content: bytes) -> GetCategorySubscriptionsErrorBody:
        match status_code:
            case 403:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


get_category_subscriptions_error_mapper: Final[
    ErrorMapper[GetCategorySubscriptionsErrorBody]
] = _GetCategorySubscriptionsError()
