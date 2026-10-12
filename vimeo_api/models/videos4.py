from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.license import LicenseOrStr
from .enums.rating import RatingOrStr
from .privacy1 import Privacy1, Privacy1Dict


class Videos4(SdkBaseModel):
    auto_generate_review_link: bool
    """Whether the user has automatic review link generation enabled by default."""

    autocc_display_enabled_by_default: bool
    """Whether the user has automatic closed captions enabled by default."""

    embed_preset_uri: Optional[str] = UNSET
    """The URI of the user's embed preset preference."""

    hide_stats: bool
    """Whether the user has hidden stats enabled by default."""

    keep_source_files: bool
    """Whether the user keeps source files after upload."""

    license: LicenseOrStr | None
    """The `Creative Commons <http://creativecommons.org/licenses/>`__ license that the user has set to be the default.

    Option descriptions:
     * ``by`` - The video is given under the Attribution license.
     * ``by-nc`` - The video is given under the Attribution Non-Commercial license.
     * ``by-nc-nd`` - The video is given under the Attribution Non-Commercial No Derivatives license.
     * ``by-nc-sa`` - The video is given under the Attribution Non-Commercial Share Alike license.
     * ``by-nd`` - The video is given under the Attribution No Derivatives license.
     * ``by-sa`` - The video is given under the Attribution Share Alike license.
     * ``cc0`` - The video is given under the Public Domain Dedication license."""

    page_preset_uri: Optional[str] = UNSET
    """The URI of the user's video page preset preference."""

    password: Optional[str] = UNSET
    """The password for viewing the authenticated user's videos."""

    privacy: Optional[Privacy1] = UNSET
    rating: RatingOrStr
    """An array of the authorized user's default content ratings.

    Option descriptions:
     * ``drugs`` - The video contains drug or alcohol use.
     * ``language`` - The video contains profanity or sexually suggestive content.
     * ``nudity`` - The video contains nudity.
     * ``safe`` - The video is suitable for all audiences.
     * ``unrated`` - The video hasn't been rated.
     * ``violence`` - The video contains violent or graphic content."""

    sharing_link_default_expiry_days: float
    """Default number of days until a sharing link expires. 0 means no expiration."""


class Videos4Dict(TypedDict):
    auto_generate_review_link: bool
    autocc_display_enabled_by_default: bool
    embed_preset_uri: NotRequired[str]
    hide_stats: bool
    keep_source_files: bool
    license: LicenseOrStr | None
    page_preset_uri: NotRequired[str]
    password: NotRequired[str]
    privacy: NotRequired[Privacy1Dict]
    rating: RatingOrStr
    sharing_link_default_expiry_days: float
