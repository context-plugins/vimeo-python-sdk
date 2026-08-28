from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class License4(str, Enum):
    """The Creative Commons license under which the video is offered.

    Option descriptions:
     * ``by`` - The video is offered under CC BY, or the attibution-only license.
     * ``by-nc`` - The video is offered under CC BY-NC, or the Attribution-NonCommercial license.
     * ``by-nc-nd`` - The video is offered under CC BY-NC-ND, or the Attribution-NonCommercian-NoDerivs license.
     * ``by-nc-sa`` - The video is offered under CC BY-NC-SA, or the Attribution-NonCommercial-ShareAlike licence.
     * ``by-nd`` - The video is offered under CC BY-ND, or the Attribution-NoDerivs license.
     * ``by-sa`` - The video is offered under CC BY-SA, or the Attribution-ShareAlike license.
     * ``cc0`` - The video is offered under CC0, or public domain, videos."""

    BY = "by"
    BY_NC = "by-nc"
    BY_NC_ND = "by-nc-nd"
    BY_NC_SA = "by-nc-sa"
    BY_ND = "by-nd"
    BY_SA = "by-sa"
    CC0 = "cc0"

    __str__ = str.__str__


License4OrStr: TypeAlias = Annotated[License4 | str, open_enum_validator(License4)]
