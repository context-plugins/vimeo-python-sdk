from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

GetWatchHistoryErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _GetWatchHistoryError:
    def map(self, response: HttpResponse) -> GetWatchHistoryErrorBody:
        match response.status_code:
            case 403:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


get_watch_history_error_mapper: Final[ErrorMapper[GetWatchHistoryErrorBody]] = _GetWatchHistoryError()
