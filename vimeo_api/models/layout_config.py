from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .grid_size import GridSize, GridSizeDict
from .show_grid_profile_image import ShowGridProfileImage, ShowGridProfileImageDict
from .show_grid_profile_name import ShowGridProfileName, ShowGridProfileNameDict
from .show_grid_section_name import ShowGridSectionName, ShowGridSectionNameDict
from .show_grid_video_count import ShowGridVideoCount, ShowGridVideoCountDict
from .show_grid_video_titles import ShowGridVideoTitles, ShowGridVideoTitlesDict


class LayoutConfig(SdkBaseModel):
    grid_size: GridSize
    """Information about the grid size configuration."""

    show_grid_profile_image: ShowGridProfileImage
    """Information about showing the profile image on each video."""

    show_grid_profile_name: ShowGridProfileName
    """Information about showing the profile name on each video."""

    show_grid_section_name: ShowGridSectionName
    """Information about showing the section names."""

    show_grid_video_count: ShowGridVideoCount
    """Information about showing the video count above the video list."""

    show_grid_video_titles: ShowGridVideoTitles
    """Information about showing the video titles below thumbnails."""


class LayoutConfigDict(TypedDict):
    grid_size: GridSizeDict
    show_grid_profile_image: ShowGridProfileImageDict
    show_grid_profile_name: ShowGridProfileNameDict
    show_grid_section_name: ShowGridSectionNameDict
    show_grid_video_count: ShowGridVideoCountDict
    show_grid_video_titles: ShowGridVideoTitlesDict
