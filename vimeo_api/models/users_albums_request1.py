from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.layout1 import Layout1OrStr
from .enums.privacy12 import Privacy12OrStr
from .enums.sort19 import Sort19OrStr
from .enums.theme import ThemeOrStr


class UsersAlbumsRequest1(SdkBaseModel):
    brand_color: Optional[str] = UNSET
    """The hexadecimal color code for the color of the player buttons and showcase controls."""

    description: Optional[str] = UNSET
    """The description of the showcase."""

    domain: OptionalNullable[str] = UNSET
    """The custom domain of the showcase."""

    hide_nav: Optional[bool] = UNSET
    """Whether to hide Vimeo navigation when displaying the showcase."""

    hide_upcoming: Optional[bool] = UNSET
    """Whether to include the upcoming event in the showcase."""

    layout: Optional[Layout1OrStr] = UNSET
    """The type of layout for presenting the showcase.

    Option descriptions:
     * ``grid`` - The videos appear in a grid.
     * ``player`` - The videos appear in the player."""

    name: Optional[str] = UNSET
    """The name of the showcase."""

    password: Optional[str] = UNSET
    """The showcase's password. This field is required only when **privacy** is ``password``."""

    privacy: Optional[Privacy12OrStr] = UNSET
    """The privacy level of the showcase.

    Option descriptions:
     * ``anybody`` - Anyone can access the showcase, either on Vimeo or through an embed.
     * ``embed_only`` - The showcase doesn't appear on Vimeo, but it can be embedded on other sites.
     * ``nobody`` - No one can access the showcase, including the authenticated user.
     * ``password`` - Only people with the password can access the showcase.
     * ``team`` - Only members of the authenticated user's team can access the showcase.
     * ``unlisted`` - The showcase can't be accessed if the URL omits its unlisted hash."""

    review_mode: Optional[bool] = UNSET
    """Whether showcase videos use the review mode URL."""

    sort: Optional[Sort19OrStr] = UNSET
    """The default sort order of the videos as they appear in the showcase.

    Option descriptions:
     * ``added_first`` - The videos appear according to when they were added to the showcase, with the most recently
            added first.
     * ``added_last`` - The videos appear according to when they were added to the showcase, with the most recently
            added last.
     * ``alphabetical`` - The videos appear alphabetically by their title.
     * ``alphabetical_desc`` - The videos appear alphabetically by their title in reverse order.
     * ``arranged`` - The videos appear as arranged by the owner of the showcase.
     * ``comments`` - The videos appear according to their number of comments.
     * ``likes`` - The videos appear according to their number of likes.
     * ``modified_time_asc`` - The videos appear in ascending order based on their last modified time.
     * ``modified_time_desc`` - The videos appear in descending order based on their last modified time.
     * ``newest`` - The videos appear in chronological order with the newest first.
     * ``oldest`` - The videos appear in chronological order with the oldest first.
     * ``plays`` - The videos appear according to their number of plays."""

    theme: Optional[ThemeOrStr] = UNSET
    """The color theme of the showcase.

    Option descriptions:
     * ``dark`` - The showcase uses the dark theme.
     * ``standard`` - The showcase uses the standard theme."""

    url: OptionalNullable[str] = UNSET
    """The custom Vimeo URL of the showcase."""

    use_custom_domain: Optional[bool] = UNSET
    """Whether the user has opted for a custom domain for their showcase."""


class UsersAlbumsRequest1Dict(TypedDict):
    brand_color: NotRequired[str]
    description: NotRequired[str]
    domain: NotRequired[str | None]
    hide_nav: NotRequired[bool]
    hide_upcoming: NotRequired[bool]
    layout: NotRequired[Layout1OrStr]
    name: NotRequired[str]
    password: NotRequired[str]
    privacy: NotRequired[Privacy12OrStr]
    review_mode: NotRequired[bool]
    sort: NotRequired[Sort19OrStr]
    theme: NotRequired[ThemeOrStr]
    url: NotRequired[str | None]
    use_custom_domain: NotRequired[bool]
