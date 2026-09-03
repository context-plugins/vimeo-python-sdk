from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

DownloadLmsPackageErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _DownloadLmsPackageError:
    def map(self, response: HttpResponse) -> DownloadLmsPackageErrorBody:
        match response.status_code:
            case 400 | 404 | 500:
                return RawError(response)
            case _:
                return RawError(response)


download_lms_package_error_mapper: Final[ErrorMapper[DownloadLmsPackageErrorBody]] = _DownloadLmsPackageError()
