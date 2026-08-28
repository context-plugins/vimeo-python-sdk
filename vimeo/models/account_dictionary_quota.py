from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .glossary_terms import GlossaryTerms, GlossaryTermsDict
from .language_replacement_terms import LanguageReplacementTerms, LanguageReplacementTermsDict


class AccountDictionaryQuota(SdkBaseModel):
    """Account dictionary usage and entry limits."""

    glossary_terms: Optional[GlossaryTerms] = UNSET
    """Glossary term usage and limit."""

    language_replacement_terms: Optional[LanguageReplacementTerms] = UNSET
    """Language replacement source-term usage and limit."""


class AccountDictionaryQuotaDict(TypedDict):
    glossary_terms: NotRequired[GlossaryTerms | GlossaryTermsDict]
    language_replacement_terms: NotRequired[LanguageReplacementTerms | LanguageReplacementTermsDict]
