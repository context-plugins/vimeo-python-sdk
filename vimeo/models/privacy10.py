from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.comments4 import Comments4OrStr
from .enums.embed11 import Embed11OrStr
from .enums.view11 import View11OrStr


class Privacy10(SdkBaseModel):
    add: Optional[bool] = UNSET
    """Whether the user can add videos to showcases, channels, or groups by default."""

    comments: Optional[Comments4OrStr] = UNSET
    """Who can comment on the user's video uploads by default.

    Option descriptions:
     * ``anybody`` - Anyone can comment.
     * ``contacts`` - Only the user's contacts can comment.
     * ``nobody`` - No one can comment."""

    download: Optional[bool] = UNSET
    """Whether the user can download videos. This value becomes the default download setting for all future videos that
    the user uploads."""

    embed: Optional[Embed11OrStr] = UNSET
    """The privacy for the user's embedded videos. The ``whitelist`` value enables you to define all valid embeddable
    domains. See our `Interacting with Videos
    <https://developer.vimeo.com/api/guides/videos/interact#set-off-site-privacy>`__ guide for details on adding and
    removing domains.

    Option descriptions:
     * ``private`` - The videos can't be embedded on any domain.
     * ``public`` - The videos can be embedded on any domain.
     * ``whitelist`` - The videos can be embedded on the specified domains only."""

    embed_allowed_domains: Optional[list[str]] = UNSET
    """An array of the user's default list of valid domains for embedding videos."""

    view: Optional[View11OrStr] = UNSET
    """Who can access the user's videos by default.

    Option descriptions:
     * ``anybody`` - Anyone can access the videos. This privacy setting appears as ``Public`` on the Vimeo front end.
     * ``contacts`` - Only the user's contacts can access the videos. _This field is deprecated._
     * ``disable`` - The videos are disabled. This privacy setting appears as ``Embed only`` on the Vimeo front end.
     * ``nobody`` - No one can access the videos. This privacy setting appears as ``Private`` on the Vimeo front end.
     * ``password`` - Only those with the password can access the videos.
     * ``unlisted`` - The videos are unlisted.
     * ``users`` - Only other Vimeo members can access the videos. _This field is deprecated._"""


class Privacy10Dict(TypedDict):
    add: NotRequired[bool]
    comments: NotRequired[Comments4OrStr]
    download: NotRequired[bool]
    embed: NotRequired[Embed11OrStr]
    embed_allowed_domains: NotRequired[list[str]]
    view: NotRequired[View11OrStr]
