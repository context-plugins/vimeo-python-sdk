from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

ExportVpaasViewerAnalyticsErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _ExportVpaasViewerAnalyticsError:
    def map(self, response: HttpResponse) -> ExportVpaasViewerAnalyticsErrorBody:
        match response.status_code:
            case 401 | 403 | 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


export_vpaas_viewer_analytics_error_mapper: Final[
    ErrorMapper[ExportVpaasViewerAnalyticsErrorBody]
] = _ExportVpaasViewerAnalyticsError()
