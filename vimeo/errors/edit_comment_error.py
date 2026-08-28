from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

EditCommentErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _EditCommentError:
    def map(self, response: HttpResponse) -> EditCommentErrorBody:
        match response.status_code:
            case 400 | 403:
                return decode_json[Error](response)
            case _:
                return RawError(response)


edit_comment_error_mapper: Final[ErrorMapper[EditCommentErrorBody]] = _EditCommentError()
