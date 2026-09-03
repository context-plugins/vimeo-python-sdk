from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error
from ..models.legacy_error import LegacyError

EditAiTexttrackErrorBody: TypeAlias = Error | LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _EditAiTexttrackError:
    def map(self, response: HttpResponse) -> EditAiTexttrackErrorBody:
        match response.status_code:
            case 400 | 503:
                return decode_json[Error](response)
            case 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


edit_ai_texttrack_error_mapper: Final[ErrorMapper[EditAiTexttrackErrorBody]] = _EditAiTexttrackError()
