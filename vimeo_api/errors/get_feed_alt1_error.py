from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetFeedAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetFeedAlt1Error:
    def map(self, response: HttpResponse) -> GetFeedAlt1ErrorBody:
        match response.status_code:
            case 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_feed_alt1_error_mapper: Final[ErrorMapper[GetFeedAlt1ErrorBody]] = _GetFeedAlt1Error()
