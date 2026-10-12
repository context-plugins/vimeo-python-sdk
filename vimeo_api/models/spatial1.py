from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .director_timeline1 import DirectorTimeline1, DirectorTimeline1Dict
from .enums.projection1 import Projection1OrStr
from .enums.stereo_format1 import StereoFormat1OrStr


class Spatial1(SdkBaseModel):
    director_timeline: Optional[list[DirectorTimeline1]] = UNSET
    """An array representing the 360 director timeline."""

    field_of_view: Optional[float] = UNSET
    """The 360 field of view. This value must be between ``30`` and ``90``; the default value is ``50``."""

    projection: Optional[Projection1OrStr] = UNSET
    """The 360 spatial projection.

    Option descriptions:
     * ``cubical`` - Use cubical projection.
     * ``cylindrical`` - Use cylindrical projection.
     * ``dome`` - Use dome projection.
     * ``equirectangular`` - Use equirectangular projection.
     * ``pyramid`` - Use pyramid projection."""

    stereo_format: Optional[StereoFormat1OrStr] = UNSET
    """The 360 spatial stereo format.

    Option descriptions:
     * ``left-right`` - Use left-right stereo.
     * ``mono`` - Use monaural audio.
     * ``top-bottom`` - Use top-bottom stereo."""


class Spatial1Dict(TypedDict):
    director_timeline: NotRequired[list[DirectorTimeline1Dict]]
    field_of_view: NotRequired[float]
    projection: NotRequired[Projection1OrStr]
    stereo_format: NotRequired[StereoFormat1OrStr]
