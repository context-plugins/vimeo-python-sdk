from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

ExportVpaasViewerAnalyticsErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _ExportVpaasViewerAnalyticsError:
    def map(self, status_code: int, content: bytes) -> ExportVpaasViewerAnalyticsErrorBody:
        match status_code:
            case 401 | 403 | 404:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


export_vpaas_viewer_analytics_error_mapper: Final[
    ErrorMapper[ExportVpaasViewerAnalyticsErrorBody]
] = _ExportVpaasViewerAnalyticsError()
