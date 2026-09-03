from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AutoCcLang(str, Enum):
    """The language in which the automated closed captions appear.

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


AutoCcLangOrStr: TypeAlias = Annotated[AutoCcLang | str, open_enum_validator(AutoCcLang)]
