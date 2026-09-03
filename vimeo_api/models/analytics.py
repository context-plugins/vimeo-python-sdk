from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .country import Country, CountryDict
from .enums.streaming_type import StreamingTypeOrStr
from .metadata12 import Metadata12, Metadata12Dict


class Analytics(SdkBaseModel):
    audio_track_language: str
    """The language of the audio track."""

    audio_track_provenance: str
    """The provenance of the audio track."""

    audio_track_type: str
    """The type of the audio track."""

    average_percent_watched: float
    """The average percent watched in seconds of the corresponding Vimeo content."""

    average_time_watched: float
    """The average time watched in seconds of the corresponding Vimeo content."""

    browser_name: str
    """The name of the browser."""

    city_name: str
    """The name of the city."""

    completions: float
    """The number of times that more than 95 percent of a video's content was played."""

    country: Country
    country_code: str
    """The country code in ISO-3166 format."""

    country_name: str
    """The name of the country."""

    device_type: str
    """The type of device."""

    downloads: float
    """The number of downloads of the corresponding Vimeo content."""

    drm_licenses_used: float
    """The number of DRM licenses used. _This field is available only to users with the DRM feature._"""

    embed_domain: str
    """The domain name of the website."""

    embed_domain_path: str
    """The path of the website URL."""

    end_date: str
    """The end time of the time interval in ISO 8601 format."""

    finishes: float
    """The number of finishes of the corresponding Vimeo content."""

    five_star_clicks: float
    """The total number of five-star ranking clicks available in each video."""

    four_star_clicks: float
    """The total number of four-star ranking clicks available in each video."""

    impressions: float
    """The number of impressions of the corresponding Vimeo content."""

    mean_percent_watched: float
    """The average percent watched in seconds of the corresponding Vimeo content."""

    mean_seconds_watched: float
    """The average time watched in seconds of the corresponding Vimeo content."""

    metadata: Metadata12
    one_star_clicks: float
    """The total number of one-star ranking clicks available in each video."""

    os_name: str
    """The name of the operating system."""

    ranking_widget_average_rating: float
    """The average ranking rating for ranking widget clicks in each video."""

    ranking_widget_clicks: float
    """The total number of ranking widget clicks available in each video."""

    region_code: str
    """The ISO 3166-2 region code."""

    region_name: str
    """The name of the region."""

    start_date: str
    """The start time of the time interval in ISO 8601 format."""

    streaming_type: StreamingTypeOrStr
    """The streaming type of the video.

    Option descriptions:
     * ``live`` - The video is streamed in real time.
     * ``non-live`` - The video isn't streamed in real time."""

    text_track_language: str
    """The language of the text track."""

    text_track_provenance: str
    """The provenance of the text track."""

    text_track_type: str
    """The type of the text track."""

    third_party_impressions: float
    """The number of impressions from all non-Vimeo players."""

    three_star_clicks: float
    """The total number of three-star ranking clicks available in each video."""

    thumbs_down_clicks: float
    """The total number of thumbs-down clicks available in each video."""

    thumbs_up_clicks: float
    """The total number of thumbs-up clicks available in each video."""

    thumbs_widget_average_rating: float
    """The average thumbs rating for thumbs widget clicks in each video."""

    thumbs_widget_clicks: float
    """The total number of thumbs widget clicks available in each video."""

    total_seconds_watched: float
    """The total time watched in seconds of the corresponding Vimeo content."""

    total_seconds_watched_including_repeats: float
    """The number of seconds watched, including repeats of the corresponding Vimeo content."""

    total_time_watched: float
    """The total time watched in seconds of the corresponding Vimeo content."""

    two_star_clicks: float
    """The total number of two-star ranking clicks available in each video."""

    unique_impressions: float
    """The number of unique impressions of the corresponding Vimeo content."""

    unique_viewers: float
    """The number of unique viewers of the corresponding Vimeo content."""

    unique_views: float
    """The number of unique views of the corresponding Vimeo content."""

    views: float
    """The number of views of the corresponding Vimeo content."""


class AnalyticsDict(TypedDict):
    audio_track_language: str
    audio_track_provenance: str
    audio_track_type: str
    average_percent_watched: float
    average_time_watched: float
    browser_name: str
    city_name: str
    completions: float
    country: Country | CountryDict
    country_code: str
    country_name: str
    device_type: str
    downloads: float
    drm_licenses_used: float
    embed_domain: str
    embed_domain_path: str
    end_date: str
    finishes: float
    five_star_clicks: float
    four_star_clicks: float
    impressions: float
    mean_percent_watched: float
    mean_seconds_watched: float
    metadata: Metadata12 | Metadata12Dict
    one_star_clicks: float
    os_name: str
    ranking_widget_average_rating: float
    ranking_widget_clicks: float
    region_code: str
    region_name: str
    start_date: str
    streaming_type: StreamingTypeOrStr
    text_track_language: str
    text_track_provenance: str
    text_track_type: str
    third_party_impressions: float
    three_star_clicks: float
    thumbs_down_clicks: float
    thumbs_up_clicks: float
    thumbs_widget_average_rating: float
    thumbs_widget_clicks: float
    total_seconds_watched: float
    total_seconds_watched_including_repeats: float
    total_time_watched: float
    two_star_clicks: float
    unique_impressions: float
    unique_viewers: float
    unique_views: float
    views: float
