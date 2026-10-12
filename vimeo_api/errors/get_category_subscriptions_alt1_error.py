from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

GetCategorySubscriptionsAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetCategorySubscriptionsAlt1Error:
    def map(self, status_code: int, content: bytes) -> GetCategorySubscriptionsAlt1ErrorBody:
        match status_code:
            case 403:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


get_category_subscriptions_alt1_error_mapper: Final[
    ErrorMapper[GetCategorySubscriptionsAlt1ErrorBody]
] = _GetCategorySubscriptionsAlt1Error()
