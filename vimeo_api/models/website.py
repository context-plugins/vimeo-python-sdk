from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Website(SdkBaseModel):
    description: Optional[str] = UNSET
    """The website's description."""

    link: str
    """The URL of the website."""

    name: Optional[str] = UNSET
    """The name of the website."""

    type_: str = Field(alias="type")
    """The URL type of the website."""

    uri: str
    """The URI of the custom website or social media page belonging to the user."""


class WebsiteDict(TypedDict):
    description: NotRequired[str]
    link: str
    name: NotRequired[str]
    type_: str
    uri: str
