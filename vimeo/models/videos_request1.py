from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .embed29 import Embed29, Embed29Dict
from .enums.license4 import License4OrStr
from .privacy20 import Privacy20, Privacy20Dict
from .review_page import ReviewPage, ReviewPageDict
from .spatial3 import Spatial3, Spatial3Dict


class VideosRequest1(SdkBaseModel):
    content_rating: Optional[list[str]] = UNSET
    """A list of values describing the content in this video. For a full list of values, use the
    https://developer.vimeo.com/api/reference/videos#get_content_ratings endpoint."""

    custom_url: Optional[str] = UNSET
    """The custom link of the video. This link doesn't include the base URL and the username or user ID of the video's
    owner."""

    description: Optional[str] = UNSET
    """The description of the video. This field can hold a maximum of 5000 characters."""

    embed: Optional[Embed29] = UNSET
    embed_domains: Optional[list[str]] = UNSET
    """The complete list of domains the video can be embedded on. This field overwrites existing domains and requires
    that **privacy_embed** have the value ``whitelist``."""

    embed_domains_add: Optional[list[str]] = UNSET
    """A list of domains intended to be added to an existing set of domains. This field requires that **privacy_embed**
    have the value ``whitelist``."""

    embed_domains_delete: Optional[list[str]] = UNSET
    """A list of domains intended to be removed from an existing set of domains. This field requires that
    **privacy_embed** have the value ``whitelist``."""

    hide_from_vimeo: Optional[bool] = UNSET
    """Whether to hide the video from everyone except the video's owner. When the value is ``true``, unlisted video
    links work only for the video's owner."""

    license: Optional[License4OrStr] = UNSET
    """The Creative Commons license under which the video is offered.

    Option descriptions:
     * ``by`` - The video is offered under CC BY, or the attibution-only license.
     * ``by-nc`` - The video is offered under CC BY-NC, or the Attribution-NonCommercial license.
     * ``by-nc-nd`` - The video is offered under CC BY-NC-ND, or the Attribution-NonCommercian-NoDerivs license.
     * ``by-nc-sa`` - The video is offered under CC BY-NC-SA, or the Attribution-NonCommercial-ShareAlike licence.
     * ``by-nd`` - The video is offered under CC BY-ND, or the Attribution-NoDerivs license.
     * ``by-sa`` - The video is offered under CC BY-SA, or the Attribution-ShareAlike license.
     * ``cc0`` - The video is offered under CC0, or public domain, videos."""

    locale: Optional[str] = UNSET
    """The video's default language. For a full list of supported languages, use the
    https://developer.vimeo.com/api/reference/videos#get_languages endpoint."""

    name: Optional[str] = UNSET
    """The title of the video. This field can hold a maximum of 128 characters."""

    password: Optional[str] = UNSET
    """The password. When you set **privacy.view** to ``password``, you must provide the password as an additional
    parameter. This field can hold a maximum of 32 characters."""

    privacy: Optional[Privacy20] = UNSET
    review_page: Optional[ReviewPage] = UNSET
    spatial: Optional[Spatial3] = UNSET


class VideosRequest1Dict(TypedDict):
    content_rating: NotRequired[list[str]]
    custom_url: NotRequired[str]
    description: NotRequired[str]
    embed: NotRequired[Embed29 | Embed29Dict]
    embed_domains: NotRequired[list[str]]
    embed_domains_add: NotRequired[list[str]]
    embed_domains_delete: NotRequired[list[str]]
    hide_from_vimeo: NotRequired[bool]
    license: NotRequired[License4OrStr]
    locale: NotRequired[str]
    name: NotRequired[str]
    password: NotRequired[str]
    privacy: NotRequired[Privacy20 | Privacy20Dict]
    review_page: NotRequired[ReviewPage | ReviewPageDict]
    spatial: NotRequired[Spatial3 | Spatial3Dict]
