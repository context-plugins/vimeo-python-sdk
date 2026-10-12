from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

DownloadLmsPackageErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _DownloadLmsPackageError:
    def map(self, status_code: int, content: bytes) -> DownloadLmsPackageErrorBody:
        match status_code:
            case 400 | 404 | 500:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


download_lms_package_error_mapper: Final[ErrorMapper[DownloadLmsPackageErrorBody]] = _DownloadLmsPackageError()
