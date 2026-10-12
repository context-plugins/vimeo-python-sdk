from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.grant_type import GrantTypeOrStr


class OauthAccessTokenRequest(SdkBaseModel):
    code: str
    """The authorization code received from the authorization server."""

    grant_type: GrantTypeOrStr
    """The grant type. The value of this field must be ``authorization_code``.

    Option descriptions:
     * ``authorization_code`` - The grant type is for an authorization code."""

    redirect_uri: str
    """The redirect URI. The value of this field must match the URI from ``/oauth/authorize``."""


class OauthAccessTokenRequestDict(TypedDict):
    code: str
    grant_type: GrantTypeOrStr
    redirect_uri: str
