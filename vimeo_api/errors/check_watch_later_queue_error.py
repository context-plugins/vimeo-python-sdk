from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

CheckWatchLaterQueueErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _CheckWatchLaterQueueError:
    def map(self, response: HttpResponse) -> CheckWatchLaterQueueErrorBody:
        match response.status_code:
            case 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


check_watch_later_queue_error_mapper: Final[ErrorMapper[CheckWatchLaterQueueErrorBody]] = _CheckWatchLaterQueueError()
