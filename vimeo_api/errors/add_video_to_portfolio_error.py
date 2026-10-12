from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.legacy_error import LegacyError

AddVideoToPortfolioErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _AddVideoToPortfolioError:
    def map(self, status_code: int, content: bytes) -> AddVideoToPortfolioErrorBody:
        match status_code:
            case 404:
                return decode_json[LegacyError](content)
            case _:
                return RawError(status_code, content)


add_video_to_portfolio_error_mapper: Final[ErrorMapper[AddVideoToPortfolioErrorBody]] = _AddVideoToPortfolioError()
