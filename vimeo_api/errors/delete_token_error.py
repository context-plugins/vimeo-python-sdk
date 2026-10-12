from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.legacy_error import LegacyError

DeleteTokenErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _DeleteTokenError:
    def map(self, status_code: int, content: bytes) -> DeleteTokenErrorBody:
        match status_code:
            case 400:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


delete_token_error_mapper: Final[ErrorMapper[DeleteTokenErrorBody]] = _DeleteTokenError()
