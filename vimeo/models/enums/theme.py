from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Theme(str, Enum):
    """The color theme of the showcase.

    Option descriptions:
     * ``dark`` - The showcase uses the dark theme.
     * ``standard`` - The showcase uses the standard theme."""

    DARK = "dark"
    STANDARD = "standard"

    __str__ = str.__str__


ThemeOrStr: TypeAlias = Annotated[Theme | str, open_enum_validator(Theme)]
