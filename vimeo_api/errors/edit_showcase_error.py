from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

EditShowcaseErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _EditShowcaseError:
    def map(self, response: HttpResponse) -> EditShowcaseErrorBody:
        match response.status_code:
            case 400 | 403 | 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


edit_showcase_error_mapper: Final[ErrorMapper[EditShowcaseErrorBody]] = _EditShowcaseError()
