from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class GrantType1(str, Enum):
    """The grant type. The value of this field must be ``client_credentials``.

    Option descriptions:
     * ``client_credentials`` - The grant type is for the client credentials."""

    CLIENT_CREDENTIALS = "client_credentials"

    __str__ = str.__str__


GrantType1OrStr: TypeAlias = Annotated[GrantType1 | str, open_enum_validator(GrantType1)]
