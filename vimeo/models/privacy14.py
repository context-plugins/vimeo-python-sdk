from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.comments5 import Comments5OrStr
from .enums.embed19 import Embed19OrStr
from .enums.view14 import View14OrStr


class Privacy14(SdkBaseModel):
    add: Optional[bool] = UNSET
    """Whether a user can add the video to a showcase, channel, or group."""

    comments: Optional[Comments5OrStr] = UNSET
    """The privacy level required to comment on the video.

    Option descriptions:
     * ``anybody`` - Anyone can comment on the video.
     * ``contacts`` - Only the video owner's contacts can comment on the video.
     * ``nobody`` - No one can comment on the video."""

    download: Optional[bool] = UNSET
    """Whether a user can download the video. This field isn't available to Vimeo Free members."""

    embed: Optional[Embed19OrStr] = UNSET
    """The video's embed setting. Specify the ``whitelist`` value to restrict embedding to a specific set of domains.
    For more information, see our `Interacting with Videos
    <https://developer.vimeo.com/api/guides/videos/interact#set-off-site-privacy>`__ guide.

    Option descriptions:
     * ``private`` - The video can't be embedded.
     * ``public`` - The video can be embedded.
     * ``whitelist`` - The video can be embedded on the specified domains only."""

    view: Optional[View14OrStr] = UNSET
    """The video's privacy setting. When this value is ``users``, ``application/json`` is the only valid content type.
    Also, some privacy settings are unavailable to Vimeo Free members; for more information, see our `Help Center
    <https://vimeo.zendesk.com/hc/en-us/articles/224817847>`__.

    Option descriptions:
     * ``anybody`` - Anyone can access the video. This privacy setting appears as ``Public`` on the Vimeo front end.
     * ``contacts`` - Only those who follow the owner on Vimeo can access the video. _This field is deprecated._
     * ``disable`` - The video is embeddable, but it's hidden on Vimeo and can't be played. This privacy setting appears
            as ``Embed only`` on the Vimeo front end.
     * ``nobody`` - No one except the owner can access the video. This privacy setting appears as ``Private`` on the
            Vimeo front end.
     * ``password`` - Only those with the password can access the video.
     * ``team`` - Anyone on the team can access the video. This privacy setting appears as ``Company only`` on the Vimeo
            front end.
     * ``unlisted`` - Only those with the private link can access the video.
     * ``users`` - Only Vimeo members can access the video. _This field is deprecated._"""


class Privacy14Dict(TypedDict):
    add: NotRequired[bool]
    comments: NotRequired[Comments5OrStr]
    download: NotRequired[bool]
    embed: NotRequired[Embed19OrStr]
    view: NotRequired[View14OrStr]
