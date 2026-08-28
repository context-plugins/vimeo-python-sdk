from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.view import ViewOrStr


class Privacy(SdkBaseModel):
    """The privacy settings of the channel."""

    view: ViewOrStr
    """The privacy setting of the channel.

    Option descriptions:
     * ``anybody`` - Anyone can access the channel. This privacy setting appears as ``Public`` on the Vimeo front end.
     * ``moderators`` - Only moderators can access the channel.
     * ``users`` - Only registered users can access the channel. _This field is deprecated._"""


class PrivacyDict(TypedDict):
    view: ViewOrStr
