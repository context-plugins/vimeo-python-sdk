from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.view6 import View6OrStr


class Privacy5(SdkBaseModel):
    """The privacy settings of the showcase."""

    password: Optional[str] = UNSET
    """The showcase's password. This field appears only when **privacy.view** is ``password``."""

    view: View6OrStr
    """The access level of the showcase.

    Option descriptions:
     * ``anybody`` - Anyone can access the showcase. This privacy setting appears as ``Public`` on the Vimeo front end.
     * ``embed_only`` - The showcase doesn't appear on Vimeo, but the owner can embed it on other sites.
     * ``nobody`` - No one can access the showacse, including the owner. This privacy setting appears as ``Private`` on
            the Vimeo front end.
     * ``password`` - Only those with the password can access the showcase.
     * ``team`` - Only the owner and members of the owner's team can access the showcase.
     * ``unlisted`` - The showcase can't be accessed if the URL omits its unlisted hash."""


class Privacy5Dict(TypedDict):
    password: NotRequired[str]
    view: View6OrStr
