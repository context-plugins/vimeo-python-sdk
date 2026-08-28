from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Domain(SdkBaseModel):
    allow_hd: bool
    """Whether to permit HD embeds on this domain."""

    domain: str
    """The domain name."""

    uri: str
    """The URI of the domain."""


class DomainDict(TypedDict):
    allow_hd: bool
    domain: str
    uri: str
