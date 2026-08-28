from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetCategorySubscriptionsErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetCategorySubscriptionsError:
    def map(self, response: HttpResponse) -> GetCategorySubscriptionsErrorBody:
        match response.status_code:
            case 403:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_category_subscriptions_error_mapper: Final[
    ErrorMapper[GetCategorySubscriptionsErrorBody]
] = _GetCategorySubscriptionsError()
