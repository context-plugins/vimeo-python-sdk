from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

EditProjectErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _EditProjectError:
    def map(self, response: HttpResponse) -> EditProjectErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


edit_project_error_mapper: Final[ErrorMapper[EditProjectErrorBody]] = _EditProjectError()
