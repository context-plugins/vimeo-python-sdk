from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Status2(SdkBaseModel):
    """An object containing data on the value of **status** and whether it's required for the interaction."""

    required: bool
    """Whether the status of the role upgrade request must be sent to achieve the desired action."""

    value: str
    """The status of the role upgrade request to which the team member should have access."""


class Status2Dict(TypedDict):
    required: bool
    value: str
