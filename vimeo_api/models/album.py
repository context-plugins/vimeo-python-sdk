from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .embed2 import Embed2, Embed2Dict
from .enums.domain_certificate_state import DomainCertificateStateOrStr
from .enums.layout import LayoutOrStr
from .enums.sort import SortOrStr
from .enums.theme import ThemeOrStr
from .metadata11 import Metadata11, Metadata11Dict
from .picture import Picture, PictureDict
from .privacy5 import Privacy5, Privacy5Dict
from .showcase_config import ShowcaseConfig, ShowcaseConfigDict
from .user import User, UserDict


class Album(SdkBaseModel):
    allow_continuous_play: bool
    """Whether the showcase permits continuous play."""

    allow_downloads: bool
    """Whether the showcase permits downloads."""

    allow_share: bool
    """Whether the showcase permits sharing."""

    allowed_privacies: list[str]
    """An array of privacy settings supported for this showcase and the requesting user."""

    autoplay: bool
    """Whether to start playback of the next video in the showcase's embedded playlist immediately after the previous
    video finishes."""

    brand_color: str | None
    """The hexadecimal color code for the color of the player buttons and showcase controls."""

    config: ShowcaseConfig
    """The showcase's configuration settings."""

    created_time: str
    """The time in ISO 8601 format when the showcase was created."""

    custom_logo: Picture | None
    """The custom logo of the showcase."""

    custom_thumbnail: Picture
    """The custom thumbnail image of the showcase."""

    description: str | None
    """A brief description of the showcase's content."""

    domain: str | None
    """The custom domain of the showcase."""

    domain_certificate_state: DomainCertificateStateOrStr
    """The state of the SSL certificate that is associated with the showcase's domain.

    Option descriptions:
     * ``0`` - The new certificate has yet to be processed.
     * ``1`` - The new certificate is being processed in the queue.
     * ``2`` - The certificate is being processed for renewal in the queue.
     * ``3`` - The new certificate has failed to be issued in the queue.
     * ``4`` - The certificate has failed to be renewed in the queue.
     * ``5`` - The certificate has been successfully issued.
     * ``6`` - The certificate has been successfully renewed.
     * ``7`` - The certificate has failed in the polling flow.
     * ``8`` - The certificate has failed to be renewed in the polling flow.
     * ``null`` - There is no associated HTTPS domain with this showcase."""

    duration: float
    """The total duration in seconds of all the videos in the showcase."""

    embed: Embed2
    """Embed data for the showcase."""

    embed_brand_color: bool | None
    """Whether to show the showcase's custom brand color in the player of the showcase's embedded playlist."""

    embed_custom_logo: bool | None
    """Whether to show the showcase's custom logo in the player of the showcase's embedded playlist."""

    has_chosen_thumbnail: bool
    """Whether the showcase has a thumbnail."""

    has_featured_content: bool
    """Whether the showcase has featured content."""

    hide_from_vimeo: bool
    """Whether the showcase should be hidden from Vimeo when unlisted."""

    hide_nav: bool
    """Whether to hide Vimeo navigation when displaying the showcase."""

    hide_upcoming: bool
    """Whether to include the upcoming event in the showcase."""

    hide_vimeo_logo: bool | None
    """Whether to hide the Vimeo logo in the player of the showcase's embedded playlist."""

    layout: LayoutOrStr
    """The type of layout for presenting the showcase.

    Option descriptions:
     * ``grid`` - The showcase videos appear in a grid.
     * ``player`` - The showcase videos appear in the player."""

    link: str
    """The URL of the showcase."""

    loop: bool
    """Whether automatic playback restarts at the top of the showcase's embedded playlist after reaching the end of the
    last video in the playlist."""

    metadata: Metadata11
    """Metadata about the showcase."""

    modified_time: str
    """The time in ISO 8601 format when the showcase was last modified."""

    name: str
    """The display name of the showcase."""

    pictures: Picture
    """The active image of the showcase."""

    privacy: Privacy5
    """The privacy settings of the showcase."""

    resource_key: str
    """The resource key of the showcase."""

    review_mode: bool
    """Whether showcase videos use the review mode URL."""

    seo_allow_indexed: bool
    """Whether search engines can index the showcase."""

    seo_description: str | None
    """The SEO description of the showcase."""

    seo_keywords: list[str]
    """The SEO keywords of the showcase."""

    seo_title: str | None
    """The SEO title of the showcase."""

    share_link: str
    """The URL for sharing the showcase."""

    sort: SortOrStr
    """The sort order of the showcase.

    Option descriptions:
     * ``added_first`` - Sort the showcase videos in order of those most recently added.
     * ``added_last`` - Sort the showcase videos in order of those least recently added.
     * ``alphabetical`` - Sort the showcase videos alphabetically.
     * ``arranged`` - Sort the showcase videos according to their custom arrangement.
     * ``comments`` - Sort the showcase videos by number of comments.
     * ``likes`` - Sort the showcase videos by number of likes.
     * ``newest`` - Sort the showcase videos in order of creation date with the newest first.
     * ``oldest`` - Sort the showcase videos in order of creation date with the oldest first.
     * ``plays`` - Sort the showcase videos by number of plays."""

    theme: ThemeOrStr
    """The color theme of the showcase.

    Option descriptions:
     * ``dark`` - The showcase uses the dark theme.
     * ``standard`` - The showcase uses the standard theme."""

    thumbnail_type: float
    """The showcase's thumbnail type. The value of this field can be ``0`` when no thumbnail is chosen, ``1`` when a
    video or event's thumbnail is chosen, ``2`` when a specific frame from a video is chosen, and ``3`` when a custom
    image is chosen."""

    total_clips: float
    """The total number of videos in the showcase."""

    unlisted_hash: Optional[str] = UNSET
    """The unlisted hash of the showcase. Omit this hash from the showcase URL to prevent access to the showcase on
    Vimeo."""

    uri: str
    """The URI of the showcase."""

    url: str | None
    """The custom Vimeo URL of the showcase."""

    use_custom_domain: bool
    """Whether the showcase uses a custom domain."""

    user: User
    """The owner of the showcase."""

    web_brand_color: bool
    """Whether to use the showcase's brand color in the web layout."""

    web_custom_logo: bool
    """Whether to use the showcase's custom logo in the web layout."""


class AlbumDict(TypedDict):
    allow_continuous_play: bool
    allow_downloads: bool
    allow_share: bool
    allowed_privacies: list[str]
    autoplay: bool
    brand_color: str | None
    config: ShowcaseConfigDict
    created_time: str
    custom_logo: PictureDict | None
    custom_thumbnail: PictureDict
    description: str | None
    domain: str | None
    domain_certificate_state: DomainCertificateStateOrStr
    duration: float
    embed: Embed2Dict
    embed_brand_color: bool | None
    embed_custom_logo: bool | None
    has_chosen_thumbnail: bool
    has_featured_content: bool
    hide_from_vimeo: bool
    hide_nav: bool
    hide_upcoming: bool
    hide_vimeo_logo: bool | None
    layout: LayoutOrStr
    link: str
    loop: bool
    metadata: Metadata11Dict
    modified_time: str
    name: str
    pictures: PictureDict
    privacy: Privacy5Dict
    resource_key: str
    review_mode: bool
    seo_allow_indexed: bool
    seo_description: str | None
    seo_keywords: list[str]
    seo_title: str | None
    share_link: str
    sort: SortOrStr
    theme: ThemeOrStr
    thumbnail_type: float
    total_clips: float
    unlisted_hash: NotRequired[str]
    uri: str
    url: str | None
    use_custom_domain: bool
    user: UserDict
    web_brand_color: bool
    web_custom_logo: bool
