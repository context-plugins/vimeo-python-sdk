from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class TextCtaAlignment(SdkBaseModel):
    """Information about the alignment of the call-to-action text on the showcase page."""

    is_upgrade: bool
    """Whether an upgrade is required to align the call-to-action text on the showcase page."""

    value: str
    """The alignment of the call-to-action text on the showcase page. Possible values include ``center`` for center
    alignment, ``left`` for left alignment, and ``right`` for right alignment."""


class TextCtaAlignmentDict(TypedDict):
    is_upgrade: bool
    value: str
