from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TitleFontFamily(str, Enum):
    """The selected video title font family."""

    ANTON = "anton"
    ARCHIVO_BLACK = "archivo_black"
    BEBAS_NEUE = "bebas_neue"
    BRICOLAGE_GROTESQUE = "bricolage_grotesque"
    CAVEAT = "caveat"
    DM_SANS = "dm_sans"
    DM_SERIF_DISPLAY = "dm_serif_display"
    FRAUNCES = "fraunces"
    HANKEN_GROTESK = "hanken_grotesk"
    IBM_PLEX_SERIF = "ibm_plex_serif"
    INSTRUMENT_SERIF = "instrument_serif"
    INTER = "inter"
    JETBRAINS_MONO = "jetbrains_mono"
    LORA = "lora"
    MONTSERRAT = "montserrat"
    OUTFIT = "outfit"
    PLAYFAIR_DISPLAY = "playfair_display"
    POPPINS = "poppins"
    ROBOTO = "roboto"
    SPACE_GROTESK = "space_grotesk"

    __str__ = str.__str__


TitleFontFamilyOrStr: TypeAlias = Annotated[TitleFontFamily | str, open_enum_validator(TitleFontFamily)]
