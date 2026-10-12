from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .director_timeline import DirectorTimeline, DirectorTimelineDict
from .enums.projection import ProjectionOrStr
from .enums.stereo_format import StereoFormatOrStr


class Spatial(SdkBaseModel):
    """The video's 360 spatial data."""

    director_timeline: Optional[list[DirectorTimeline]] = UNSET
    """The video's 360 director timeline."""

    field_of_view: OptionalNullable[float] = UNSET
    """The video's 360 field of view value, ranging from a mininum of ``30`` to a maximum of ``90``. The default value
    is ``50``."""

    projection: OptionalNullable[ProjectionOrStr] = UNSET
    """The video's 360 spatial projection.

    Option descriptions:
     * ``cubical`` - The spatial projection is cubical.
     * ``cylindrical`` - The spatial projection is cylindrical.
     * ``dome`` - The spatial projection is dome-shaped.
     * ``equirectangular`` - The spatial projection is equirectangular.
     * ``pyramid`` - The spatial projection is pyramid-shaped."""

    stereo_format: OptionalNullable[StereoFormatOrStr] = UNSET
    """The video's 360 stereo format.

    Option descriptions:
     * ``left-right`` - The stereo format is left-right.
     * ``mono`` - The audio is monaural.
     * ``top-bottom`` - The stereo format is top-bottom."""


class SpatialDict(TypedDict):
    director_timeline: NotRequired[list[DirectorTimelineDict]]
    field_of_view: NotRequired[float | None]
    projection: NotRequired[ProjectionOrStr | None]
    stereo_format: NotRequired[StereoFormatOrStr | None]
