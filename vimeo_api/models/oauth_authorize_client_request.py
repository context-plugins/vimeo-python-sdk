from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.grant_type1 import GrantType1OrStr


class OauthAuthorizeClientRequest(SdkBaseModel):
    grant_type: GrantType1OrStr
    """The grant type. The value of this field must be ``client_credentials``.

    Option descriptions:
     * ``client_credentials`` - The grant type is for the client credentials."""

    scope: str
    """A space-separated list of the authentication scopes to access. The default is ``public``."""


class OauthAuthorizeClientRequestDict(TypedDict):
    grant_type: GrantType1OrStr
    scope: str
