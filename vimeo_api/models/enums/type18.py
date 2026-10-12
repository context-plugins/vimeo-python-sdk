from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type18(str, Enum):
    """Which logo to show in the landing page navbar.

    Option descriptions:
     * ``custom`` - A custom brand-kit logo (see ``uri``/``url``).
     * ``none`` - No logo is shown.
     * ``vimeo`` - The Vimeo logo."""

    CUSTOM = "custom"
    NONE = "none"
    VIMEO = "vimeo"

    __str__ = str.__str__


Type18OrStr: TypeAlias = Annotated[Type18 | str, open_enum_validator(Type18)]
