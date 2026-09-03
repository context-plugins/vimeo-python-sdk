from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class GlossaryTerms(SdkBaseModel):
    """Glossary term usage and limit."""

    limit: Optional[float] = UNSET
    """The maximum number of glossary terms permitted for the account."""

    used: Optional[float] = UNSET
    """The number of active glossary terms."""


class GlossaryTermsDict(TypedDict):
    limit: NotRequired[float]
    used: NotRequired[float]
