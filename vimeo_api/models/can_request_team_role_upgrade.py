from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .properties import Properties, PropertiesDict


class CanRequestTeamRoleUpgrade(SdkBaseModel):
    """Information about whether the user can request a team upgrade from the Viewer role."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    properties: Properties
    """An object of suggested fields to be used for this interaction."""

    uri: str
    """The API URI that resolves to the connection data."""


class CanRequestTeamRoleUpgradeDict(TypedDict):
    options: list[str]
    properties: PropertiesDict
    uri: str
