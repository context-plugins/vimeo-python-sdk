from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error
from ..models.legacy_error import LegacyError

UpdateCustomMetadataFieldOptionsErrorBody: TypeAlias = Error | LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _UpdateCustomMetadataFieldOptionsError:
    def map(self, response: HttpResponse) -> UpdateCustomMetadataFieldOptionsErrorBody:
        match response.status_code:
            case 400:
                return decode_json[Error](response)
            case 401 | 403:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


update_custom_metadata_field_options_error_mapper: Final[
    ErrorMapper[UpdateCustomMetadataFieldOptionsErrorBody]
] = _UpdateCustomMetadataFieldOptionsError()
