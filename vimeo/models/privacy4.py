from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.comment2 import Comment2OrStr
from .enums.invite2 import Invite2OrStr
from .enums.join1 import Join1OrStr
from .enums.videos7 import Videos7OrStr
from .enums.view5 import View5OrStr


class Privacy4(SdkBaseModel):
    """The group's privacy settings."""

    comment: Comment2OrStr
    """Who can comment on the group.

    Option descriptions:
     * ``all`` - Anyone can comment on the group.
     * ``members`` - Only group members can comment on the group."""

    invite: Invite2OrStr
    """Who can invite new members to the group.

    Option descriptions:
     * ``all`` - Anyone can invite new members to the group.
     * ``members`` - Only group members can invite new members to the group."""

    join: Join1OrStr
    """Who can join the group.

    Option descriptions:
     * ``anybody`` - Anyone can join the group.
     * ``members`` - Only people with a Vimeo account can join the group."""

    videos: Videos7OrStr
    """Who can add videos to the group.

    Option descriptions:
     * ``all`` - Anyone can add videos to the group.
     * ``members`` - Only group members can add videos to the group."""

    view: View5OrStr
    """Who can access the group.

    Option descriptions:
     * ``anybody`` - Anyone can access the group. This privacy setting appears as ``Public`` on the Vimeo front end.
     * ``members`` - Only group members can access the group."""


class Privacy4Dict(TypedDict):
    comment: Comment2OrStr
    invite: Invite2OrStr
    join: Join1OrStr
    videos: Videos7OrStr
    view: View5OrStr
