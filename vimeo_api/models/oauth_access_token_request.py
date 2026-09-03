from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class OauthAccessTokenRequest(SdkBaseModel):
    code: str
    """The authorization code received from the authorization server."""

    grant_type: Literal["authorization_code"] = "authorization_code"
    """The grant type. The value of this field must be ``authorization_code``.

    Option descriptions:
     * ``authorization_code`` - The grant type is for an authorization code."""

    redirect_uri: str
    """The redirect URI. The value of this field must match the URI from ``/oauth/authorize``."""


class OauthAccessTokenRequestDict(TypedDict):
    code: str
    grant_type: NotRequired[Literal["authorization_code"]]
    redirect_uri: str
