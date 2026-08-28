from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .buy3 import Buy3, Buy3Dict
from .enums.accepted_currencies import AcceptedCurrenciesOrStr
from .enums.content_rating1 import ContentRating1OrStr
from .enums.type37 import Type37OrStr
from .episodes1 import Episodes1, Episodes1Dict
from .rent4 import Rent4, Rent4Dict
from .subscription2 import Subscription2, Subscription2Dict


class MeOndemandPagesRequest(SdkBaseModel):
    accepted_currencies: Optional[AcceptedCurrenciesOrStr] = UNSET
    """An array of accepted currencies.

    Option descriptions:
     * ``AUD`` - The currency is in Australian dollars.
     * ``CAD`` - The currency is in Canadian dollars.
     * ``CHF`` - The currency is in Swiss francs.
     * ``DKK`` - The currency is in Danish krone.
     * ``EUR`` - The currency is in euros.
     * ``GBP`` - The currency is in British pounds.
     * ``JPY`` - The currency is in Japanese yen.
     * ``KRW`` - The currency is in South Korean won.
     * ``NOK`` - The currency is in Norwegian krone.
     * ``PLN`` - The currency is in Polish zloty.
     * ``SEK`` - The currency is in Swedish krona.
     * ``USD`` - The currency is in United States dollars."""

    buy: Optional[Buy3] = UNSET
    content_rating: ContentRating1OrStr
    """The content rating of the video, given either as a comma-separated list or as a JSON array, depending on the
    request format.

    Option descriptions:
     * ``drugs`` - The video contains drug or alcohol use.
     * ``language`` - The video contains profanity or sexually suggestive content.
     * ``nudity`` - The video contains nudity.
     * ``safe`` - The video is suitable for all audiences.
     * ``unrated`` - The video hasn't been rated.
     * ``violence`` - The video contains violent or graphic content."""

    description: str
    """The description of the On Demand page."""

    domain_link: Optional[str] = UNSET
    """The custom domain of the On Demand page."""

    episodes: Optional[Episodes1] = UNSET
    link: Optional[str] = UNSET
    """The custom string to use in the Vimeo URL of the On Demand page."""

    name: str
    """The name of the On Demand page."""

    rent: Optional[Rent4] = UNSET
    subscription: Optional[Subscription2] = UNSET
    type_: Type37OrStr = Field(alias="type")
    """The type of the On Demand page.

    Option descriptions:
     * ``film`` - The On Demand page is a film.
     * ``series`` - The On Demand page is a series."""


class MeOndemandPagesRequestDict(TypedDict):
    accepted_currencies: NotRequired[AcceptedCurrenciesOrStr]
    buy: NotRequired[Buy3 | Buy3Dict]
    content_rating: ContentRating1OrStr
    description: str
    domain_link: NotRequired[str]
    episodes: NotRequired[Episodes1 | Episodes1Dict]
    link: NotRequired[str]
    name: str
    rent: NotRequired[Rent4 | Rent4Dict]
    subscription: NotRequired[Subscription2 | Subscription2Dict]
    type_: Type37OrStr
