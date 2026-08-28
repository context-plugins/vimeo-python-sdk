from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .add import Add, AddDict
from .remove import Remove, RemoveDict


class VideosAlbumsRequest(SdkBaseModel):
    add: Optional[list[Add]] = UNSET
    """The array of showcases to add the video to. Specify these with a batch request; see our `Using Common Formats and
    Parameters <https://developer.vimeo.com/api/common-formats#working-with-batch-requests>`__ guide for more
    information."""

    remove: Optional[list[Remove]] = UNSET
    """The array of showcases to remove the video from. Specify these with a batch request; see our `Using Common
    Formats and Parameters <https://developer.vimeo.com/api/common-formats#working-with-batch-requests>`__ guide for
    more information."""


class VideosAlbumsRequestDict(TypedDict):
    add: NotRequired[list[Add | AddDict]]
    remove: NotRequired[list[Remove | RemoveDict]]
