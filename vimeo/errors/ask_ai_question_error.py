from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error
from ..models.legacy_error import LegacyError

AskAiQuestionErrorBody: TypeAlias = Error | LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _AskAiQuestionError:
    def map(self, response: HttpResponse) -> AskAiQuestionErrorBody:
        match response.status_code:
            case 400 | 403 | 503:
                return decode_json[Error](response)
            case 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


ask_ai_question_error_mapper: Final[ErrorMapper[AskAiQuestionErrorBody]] = _AskAiQuestionError()
