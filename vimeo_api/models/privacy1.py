from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.comments import CommentsOrStr
from .enums.embed import EmbedOrStr
from .enums.view1 import View1OrStr


class Privacy1(SdkBaseModel):
    add: Optional[bool] = UNSET
    """Whether other users can add the authenticated user's videos."""

    allow_share_link: Optional[bool] = UNSET
    """Whether unlisted videos are hidden from Vimeo."""

    clip_embed_allowed_domains: Optional[list[str]] = UNSET
    """The list of domains where the authenticated user can embed the video."""

    comments: Optional[CommentsOrStr] = UNSET
    """The authenticated user's privacy preference for comments.

    Option descriptions:
     * ``anybody`` - Anyone can comment on the user's videos.
     * ``contacts`` - Only contacts can comment on the user's videos.
     * ``nobody`` - No one can comment on the user's videos."""

    download: Optional[bool] = UNSET
    """Whether other users can download the authenticated user's videos."""

    embed: Optional[EmbedOrStr] = UNSET
    """The authenticated user's privacy preference for embeds.

    Option descriptions:
     * ``private`` - Only the user can embed their own videos.
     * ``public`` - Anyone can embed the user's videos.
     * ``whitelist`` - Only specified users can embed the user's videos."""

    password: Optional[str] = UNSET
    """The default password for the video."""

    view: Optional[View1OrStr] = UNSET
    """The authenticated user's privacy preference for views.

    Option descriptions:
     * ``anybody`` - Anyone can view the user's videos. This privacy setting appears as ``Public`` on the Vimeo front
            end.
     * ``contacts`` - Only contacts can view the user's videos. _This field is deprecated._
     * ``disable`` - Views are disabled for the user's videos. This privacy setting appears as ``Embed only`` on the
            Vimeo front end.
     * ``nobody`` - No one except the user can view the user's videos. This privacy setting appears as ``Private`` on
            the Vimeo front end.
     * ``password`` - Only those with the password can view the user's videos.
     * ``unlisted`` - Anybody can view the user's videos if they have a link.
     * ``users`` - Only other Vimeo members can view the user's videos. _This field is deprecated._"""


class Privacy1Dict(TypedDict):
    add: NotRequired[bool]
    allow_share_link: NotRequired[bool]
    clip_embed_allowed_domains: NotRequired[list[str]]
    comments: NotRequired[CommentsOrStr]
    download: NotRequired[bool]
    embed: NotRequired[EmbedOrStr]
    password: NotRequired[str]
    view: NotRequired[View1OrStr]
