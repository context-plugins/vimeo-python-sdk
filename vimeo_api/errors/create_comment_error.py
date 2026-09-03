from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

CreateCommentErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _CreateCommentError:
    def map(self, response: HttpResponse) -> CreateCommentErrorBody:
        match response.status_code:
            case 400 | 401 | 403:
                return decode_json[Error](response)
            case _:
                return RawError(response)


create_comment_error_mapper: Final[ErrorMapper[CreateCommentErrorBody]] = _CreateCommentError()
