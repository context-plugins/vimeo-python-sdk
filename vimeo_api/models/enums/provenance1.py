from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Provenance1(str, Enum):
    """The upload source of the text track.

    Option descriptions:
     * ``autogen_alternate_audio`` - The text track is automatically generated from alternate audio.
     * ``autogen_dubbed`` - The text track is automatically generated from AI dubbing.
     * ``autogen_live_audio`` - The text track is automatically generated from live audio.
     * ``autogen_source_audio`` - The text track is automatically generated from source audio.
     * ``autogen_translated`` - The text track is automatically generated from AI translation.
     * ``user_uploaded`` - The text track is uploaded by a user."""

    AUTOGEN_ALTERNATE_AUDIO = "autogen_alternate_audio"
    AUTOGEN_DUBBED = "autogen_dubbed"
    AUTOGEN_LIVE_AUDIO = "autogen_live_audio"
    AUTOGEN_SOURCE_AUDIO = "autogen_source_audio"
    AUTOGEN_TRANSLATED = "autogen_translated"
    USER_UPLOADED = "user_uploaded"

    __str__ = str.__str__


Provenance1OrStr: TypeAlias = Annotated[Provenance1 | str, open_enum_validator(Provenance1)]
