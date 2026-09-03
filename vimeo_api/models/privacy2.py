from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.view3 import View3OrStr


class Privacy2(SdkBaseModel):
    """The privacy settings of the folder."""

    view: View3OrStr
    """The privacy setting for accessing the folder.

    Option descriptions:
     * ``anybody`` - Anyone with the link can access the contents of the folder. This privacy setting appears as
            ``Public`` on the Vimeo front end.
     * ``nobody`` - Only the owner and those team members that the owner has explicitly invited can access the contents
            of the folder. This privacy setting appears as ``Private`` on the Vimeo front end.
     * ``team`` - Only those team members with the link can access the contents of the folder."""


class Privacy2Dict(TypedDict):
    view: View3OrStr
