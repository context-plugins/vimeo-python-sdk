from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

FederatedSearchUserItemsAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _FederatedSearchUserItemsAlt1Error:
    def map(self, status_code: int, content: bytes) -> FederatedSearchUserItemsAlt1ErrorBody:
        match status_code:
            case 401:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


federated_search_user_items_alt1_error_mapper: Final[
    ErrorMapper[FederatedSearchUserItemsAlt1ErrorBody]
] = _FederatedSearchUserItemsAlt1Error()
