from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.action import ActionOrStr


class Context(SdkBaseModel):
    """The context of the video's subscription, if the video is part of a subscription."""

    action: ActionOrStr
    """The relevant contextual action.

    Option descriptions:
     * ``Added to`` - An Added To action.
     * ``Appearance by`` - An Appearance By action.
     * ``Liked by`` - A Liked By action.
     * ``Uploaded by`` - An Uploaded By action."""

    resource: Any | None
    """The contextual resource: a user, group, or channel representation, or an object of a tag."""

    resource_type: str
    """The contextual resource type."""


class ContextDict(TypedDict):
    action: ActionOrStr
    resource: Any | None
    resource_type: str
