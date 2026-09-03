from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error
from ..models.legacy_error import LegacyError

DeleteCommentErrorBody: TypeAlias = Error | LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _DeleteCommentError:
    def map(self, response: HttpResponse) -> DeleteCommentErrorBody:
        match response.status_code:
            case 403:
                return decode_json[Error](response)
            case 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


delete_comment_error_mapper: Final[ErrorMapper[DeleteCommentErrorBody]] = _DeleteCommentError()
