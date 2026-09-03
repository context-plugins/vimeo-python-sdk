from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.legacy_error import LegacyError

DeleteVideoFromPortfolioAlt1ErrorBody: TypeAlias = LegacyError | RawError


@dataclass(frozen=True, slots=True)
class _DeleteVideoFromPortfolioAlt1Error:
    def map(self, response: HttpResponse) -> DeleteVideoFromPortfolioAlt1ErrorBody:
        match response.status_code:
            case 404:
                return decode_json[LegacyError](response)
            case _:
                return RawError(response)


delete_video_from_portfolio_alt1_error_mapper: Final[
    ErrorMapper[DeleteVideoFromPortfolioAlt1ErrorBody]
] = _DeleteVideoFromPortfolioAlt1Error()
