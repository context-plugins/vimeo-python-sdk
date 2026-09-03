from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

DeleteProjectAlt1ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _DeleteProjectAlt1Error:
    def map(self, response: HttpResponse) -> DeleteProjectAlt1ErrorBody:
        match response.status_code:
            case 401 | 403 | 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


delete_project_alt1_error_mapper: Final[ErrorMapper[DeleteProjectAlt1ErrorBody]] = _DeleteProjectAlt1Error()
