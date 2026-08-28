from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error
from ..models.legacy_error import LegacyError

JoinGroupErrorBody: TypeAlias = LegacyError | Error | RawError


@dataclass(frozen=True, slots=True)
class _JoinGroupError:
    def map(self, response: HttpResponse) -> JoinGroupErrorBody:
        match response.status_code:
            case 403:
                return decode_json[LegacyError](response)
            case 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


join_group_error_mapper: Final[ErrorMapper[JoinGroupErrorBody]] = _JoinGroupError()
