from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LanguageReplacementTerms(SdkBaseModel):
    """Language replacement source-term usage and limit."""

    limit: Optional[float] = UNSET
    """The maximum number of language replacement source terms permitted for the account."""

    used: Optional[float] = UNSET
    """The number of distinct active language replacement source terms."""


class LanguageReplacementTermsDict(TypedDict):
    limit: NotRequired[float]
    used: NotRequired[float]
