from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.comments2 import Comments2OrStr
from .enums.embed1 import Embed1OrStr
from .enums.view4 import View4OrStr


class Privacy3(SdkBaseModel):
    """The video's privacy setting."""

    add: bool
    """Whether the video can be added to collections."""

    allow_share_link: bool
    """Whether the share link is usable."""

    comments: Comments2OrStr
    """The video's comment permission setting.

    Option descriptions:
     * ``anybody`` - Anyone can comment on the video.
     * ``contacts`` - Only contacts can comment on the video.
     * ``nobody`` - No one can comment on the video."""

    download: bool
    """Whether the video can be downloaded."""

    embed: Embed1OrStr
    """The video's embed permission setting.

    Option descriptions:
     * ``private`` - The video is private.
     * ``public`` - Anyone can embed the video.
     * ``whitelist`` - The video can be embedded on specific domains."""

    original_view: Optional[str] = UNSET
    """The original privacy setting the video had before its current privacy was restricted by the owner's plan.
    Populated in two cases: for cold-storage videos (``privacy.view = "purgatory"``), the privacy the video had before
    being moved to cold storage; for cold-privacy videos (``is_cold_privacy_restricted = true``), the original premium
    privacy (for example ``unlisted``) that the free plan no longer supports while ``privacy.view`` is collapsed to
    ``nobody``. Absent for videos that aren't restricted."""

    view: View4OrStr
    """The general privacy setting of the video.

    Option descriptions:
     * ``anybody`` - Anyone can access the video. This privacy setting appears as ``Public`` on the Vimeo front end.
     * ``cold_storage`` - The video is temporarily frozen because the owner exceeded their plan's storage limit. The
            video page renders with an in-player overlay.
     * ``contacts`` - Only contacts can access the video. _This field is deprecated._
     * ``disable`` - The video is hidden from Vimeo. This privacy setting appears as ``Embed only`` on the Vimeo front
            end.
     * ``nobody`` - No one besides the owner can access the video. This privacy setting appears as ``Private`` on the
            Vimeo front end.
     * ``password`` - Anyone with the video's password can access the video.
     * ``ptv`` - The Vimeo On Demand video is accessible and searchable from Vimeo. _This field is deprecated._
     * ``ptvhide`` - The Vimeo On Demand video is hidden from Vimeo. _This field is deprecated._
     * ``stock`` - The stock footage is accessible and searchable from Vimeo. _This field is deprecated._
     * ``stock_purchased`` - The purchased stock footage is accessible and searchable from Vimeo. _This field is
            deprecated._
     * ``team`` - Anyone on the team can access the video. This privacy setting appears as ``Company only`` on the Vimeo
            front end.
     * ``unlisted`` - The video is accessible but not searchable from Vimeo.
     * ``users`` - Only Vimeo members can access the video. _This field is deprecated._"""


class Privacy3Dict(TypedDict):
    add: bool
    allow_share_link: bool
    comments: Comments2OrStr
    download: bool
    embed: Embed1OrStr
    original_view: NotRequired[str]
    view: View4OrStr
