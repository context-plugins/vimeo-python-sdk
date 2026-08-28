from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class View3(str, Enum):
    """The privacy setting for accessing the folder.

    Option descriptions:
     * ``anybody`` - Anyone with the link can access the contents of the folder. This privacy setting appears as
            ``Public`` on the Vimeo front end.
     * ``nobody`` - Only the owner and those team members that the owner has explicitly invited can access the contents
            of the folder. This privacy setting appears as ``Private`` on the Vimeo front end.
     * ``team`` - Only those team members with the link can access the contents of the folder."""

    ANYBODY = "anybody"
    NOBODY = "nobody"
    TEAM = "team"

    __str__ = str.__str__


View3OrStr: TypeAlias = Annotated[View3 | str, open_enum_validator(View3)]
