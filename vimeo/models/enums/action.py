from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Action(str, Enum):
    """The relevant contextual action.

    Option descriptions:
     * ``Added to`` - An Added To action.
     * ``Appearance by`` - An Appearance By action.
     * ``Liked by`` - A Liked By action.
     * ``Uploaded by`` - An Uploaded By action."""

    ADDED_TO = "Added to"
    APPEARANCE_BY = "Appearance by"
    LIKED_BY = "Liked by"
    UPLOADED_BY = "Uploaded by"

    __str__ = str.__str__


ActionOrStr: TypeAlias = Annotated[Action | str, open_enum_validator(Action)]
