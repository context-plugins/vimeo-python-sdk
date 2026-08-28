from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .embed18 import Embed18, Embed18Dict
from .enums.license2 import License2OrStr
from .privacy14 import Privacy14, Privacy14Dict
from .review_page import ReviewPage, ReviewPageDict
from .spatial1 import Spatial1, Spatial1Dict
from .upload2 import Upload2, Upload2Dict


class UsersVideosRequest1(SdkBaseModel):
    content_rating: Optional[list[str]] = UNSET
    """A list of values describing the content in this video. For a full list of values, use the
    https://developer.vimeo.com/api/reference/videos#get_content_ratings endpoint."""

    description: Optional[str] = UNSET
    """The description of the video."""

    embed: Optional[Embed18] = UNSET
    embed_domains: Optional[list[str]] = UNSET
    """The complete list of domains the video can be embedded on. This field requires that **privacy_embed** have the
    value ``whitelist``."""

    folder_uri: Optional[str] = UNSET
    """The URI of the folder to which the video is uploaded."""

    hide_from_vimeo: Optional[bool] = UNSET
    """Whether to hide the video from everyone except the video's owner. When the value is ``true``, unlisted video
    links work only for the video's owner."""

    license: Optional[License2OrStr] = UNSET
    """The Creative Commons license under which the video is offered.

    Option descriptions:
     * ``by`` - The video is offered under CC BY, or the attibution-only license.
     * ``by-nc`` - The video is offered under CC BY-NC, or the Attribution-NonCommercial license.
     * ``by-nc-nd`` - The video is offered under CC BY-NC-ND, or the Attribution-NonCommercian-NoDerivs license.
     * ``by-nc-sa`` - The video is offered under CC BY-NC-SA, or the Attribution-NonCommercial-ShareAlike licence.
     * ``by-nd`` - The video is offered under CC BY-ND, or the Attribution-NoDerivs license.
     * ``by-sa`` - The video is offered under CC BY-SA, or the Attribution-ShareAlike license.
     * ``cc0`` - The video is offered under CC0, or the public domain license."""

    locale: Optional[str] = UNSET
    """The video's default language. For a full list of supported languages, use the
    https://developer.vimeo.com/api/reference/videos#get_languages endpoint."""

    name: Optional[str] = UNSET
    """The title of the video."""

    password: Optional[str] = UNSET
    """The password. This field is required when **privacy.view** is ``password``."""

    privacy: Optional[Privacy14] = UNSET
    review_page: Optional[ReviewPage] = UNSET
    spatial: Optional[Spatial1] = UNSET
    upload: Upload2


class UsersVideosRequest1Dict(TypedDict):
    content_rating: NotRequired[list[str]]
    description: NotRequired[str]
    embed: NotRequired[Embed18 | Embed18Dict]
    embed_domains: NotRequired[list[str]]
    folder_uri: NotRequired[str]
    hide_from_vimeo: NotRequired[bool]
    license: NotRequired[License2OrStr]
    locale: NotRequired[str]
    name: NotRequired[str]
    password: NotRequired[str]
    privacy: NotRequired[Privacy14 | Privacy14Dict]
    review_page: NotRequired[ReviewPage | ReviewPageDict]
    spatial: NotRequired[Spatial1 | Spatial1Dict]
    upload: Upload2 | Upload2Dict
