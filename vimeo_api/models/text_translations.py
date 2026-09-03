from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.reason7 import Reason7OrStr


class TextTranslations(SdkBaseModel):
    """Information about where and how to create a text translation for the video."""

    disabled: bool
    """Whether the translation method is disabled."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    reason: Reason7OrStr | None
    """The reason why the translation method is disabled.

    Option descriptions:
     * ``owner_account_blocked`` - The owner account is blocked due to billing issues.
     * ``owner_disabled_feature_group`` - The owner has disabled the feature group.
     * ``owner_payment_disabled`` - The owner account can't use the payments service.
     * ``transcript_status_does_not_exist`` - The video transcript doesn't exist."""

    uri: str
    """The API URI that resolves to the connection data."""


class TextTranslationsDict(TypedDict):
    disabled: bool
    options: list[str]
    reason: Reason7OrStr | None
    uri: str
