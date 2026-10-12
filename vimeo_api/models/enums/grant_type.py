from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class GrantType(str, Enum):
    """The grant type. The value of this field must be ``authorization_code``.

    Option descriptions:
     * ``authorization_code`` - The grant type is for an authorization code."""

    AUTHORIZATION_CODE = "authorization_code"

    __str__ = str.__str__


GrantTypeOrStr: TypeAlias = Annotated[GrantType | str, open_enum_validator(GrantType)]
