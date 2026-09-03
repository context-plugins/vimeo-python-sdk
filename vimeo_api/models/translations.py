from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.reason8 import Reason8OrStr


class Translations(SdkBaseModel):
    """Information about where and how to create a translation for the video."""

    disabled: bool
    """Whether the translation method is disabled."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    reason: Reason8OrStr | None
    """The reason why the translation method is disabled.

    Option descriptions:
     * ``language_not_supported`` - The video language isn't supported.
     * ``owner_account_blocked`` - The owner account is blocked due to billing issues.
     * ``owner_disabled_feature_group`` - The owner has disabled the feature group.
     * ``video_too_long`` - The video is too long."""

    uri: str
    """The API URI that resolves to the connection data."""


class TranslationsDict(TypedDict):
    disabled: bool
    options: list[str]
    reason: Reason8OrStr | None
    uri: str
