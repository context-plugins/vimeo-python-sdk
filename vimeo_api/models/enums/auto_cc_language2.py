from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AutoCcLanguage2(str, Enum):
    """The language of the automated closed captions.

    Option descriptions:
     * ``de-DE`` - The language is German.
     * ``en-US`` - The language is English.
     * ``es-ES`` - The language is Spanish.
     * ``fr-FR`` - The language is French.
     * ``pt-BR`` - The language is Portuguese."""

    DE_DE = "de-DE"
    EN_US = "en-US"
    ES_ES = "es-ES"
    FR_FR = "fr-FR"
    PT_BR = "pt-BR"

    __str__ = str.__str__


AutoCcLanguage2OrStr: TypeAlias = Annotated[AutoCcLanguage2 | str, open_enum_validator(AutoCcLanguage2)]
