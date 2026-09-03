from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Sort22(str, Enum):
    COMMENTS = "comments"
    COMPLETIONS = "completions"
    COUNTRY = "country"
    DEFAULT = "default"
    DEVICE_TYPE = "device_type"
    DOWNLOADS = "downloads"
    DRM_LICENSES_USED = "drm_licenses_used"
    EMBED_DOMAIN = "embed_domain"
    FINISHES = "finishes"
    FIVE_STAR_CLICKS = "five_star_clicks"
    FOUR_STAR_CLICKS = "four_star_clicks"
    IMPRESSIONS = "impressions"
    LIKE = "like"
    MEAN_PERCENT_WATCHED = "mean_percent_watched"
    MEAN_SECONDS_WATCHED = "mean_seconds_watched"
    ONE_STAR_CLICKS = "one_star_clicks"
    RANKING_WIDGET_AVERAGE_RATING = "ranking_widget_average_rating"
    RANKING_WIDGET_CLICKS = "ranking_widget_clicks"
    THIRD_PARTY_IMPRESSIONS = "third_party_impressions"
    THREE_STAR_CLICKS = "three_star_clicks"
    THUMBS_DOWN_CLICKS = "thumbs_down_clicks"
    THUMBS_UP_CLICKS = "thumbs_up_clicks"
    THUMBS_WIDGET_AVERAGE_RATING = "thumbs_widget_average_rating"
    THUMBS_WIDGET_CLICKS = "thumbs_widget_clicks"
    TIME = "time"
    TOTAL_SECONDS_WATCHED = "total_seconds_watched"
    TWO_STAR_CLICKS = "two_star_clicks"
    UNIQUE_IMPRESSIONS = "unique_impressions"
    UNIQUE_VIEWERS = "unique_viewers"
    VIDEO = "video"
    VIEWS = "views"

    __str__ = str.__str__


Sort22OrStr: TypeAlias = Annotated[Sort22 | str, open_enum_validator(Sort22)]
