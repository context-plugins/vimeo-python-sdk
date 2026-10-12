from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

EditLiveEventAutoCcAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _EditLiveEventAutoCcAlt1Error:
    def map(self, status_code: int, content: bytes) -> EditLiveEventAutoCcAlt1ErrorBody:
        match status_code:
            case 400 | 403 | 404:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


edit_live_event_auto_cc_alt1_error_mapper: Final[
    ErrorMapper[EditLiveEventAutoCcAlt1ErrorBody]
] = _EditLiveEventAutoCcAlt1Error()
