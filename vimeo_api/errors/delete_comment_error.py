from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error
from ..models.legacy_error import LegacyError

DeleteCommentErrorBody: TypeAlias = Error | LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _DeleteCommentError:
    def map(self, status_code: int, content: bytes) -> DeleteCommentErrorBody:
        match status_code:
            case 403:
                return decode_json[Error](content)
            case 404:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


delete_comment_error_mapper: Final[ErrorMapper[DeleteCommentErrorBody]] = _DeleteCommentError()
