from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

EditCommentErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _EditCommentError:
    def map(self, status_code: int, content: bytes) -> EditCommentErrorBody:
        match status_code:
            case 400 | 403:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


edit_comment_error_mapper: Final[ErrorMapper[EditCommentErrorBody]] = _EditCommentError()
