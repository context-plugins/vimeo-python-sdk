from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

FederatedSearchUserItemsErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _FederatedSearchUserItemsError:
    def map(self, response: HttpResponse) -> FederatedSearchUserItemsErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


federated_search_user_items_error_mapper: Final[
    ErrorMapper[FederatedSearchUserItemsErrorBody]
] = _FederatedSearchUserItemsError()
