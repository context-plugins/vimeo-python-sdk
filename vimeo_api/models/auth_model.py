from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .api_app import ApiApp, ApiAppDict
from .user import User, UserDict


class AuthModel(SdkBaseModel):
    access_token: str
    """The access token string."""

    app: ApiApp
    """The API application associated with the token."""

    expires_on: Optional[str] = UNSET
    """The token's expiration date."""

    refresh_token: Optional[str] = UNSET
    """The refresh token string. The Vimeo API doesn't currently support refresh tokens, but we plan to add this support
    in the future."""

    scope: str
    """The scope or scopes that the token supports."""

    token_type: Literal["bearer"] = "bearer"
    """The token type.

    Option descriptions:
     * ``bearer`` - The token is of the bearer type."""

    user: Optional[User] = UNSET
    """The user associated with the token."""


class AuthModelDict(TypedDict):
    access_token: str
    app: ApiApp | ApiAppDict
    expires_on: NotRequired[str]
    refresh_token: NotRequired[str]
    scope: str
    token_type: NotRequired[Literal["bearer"]]
    user: NotRequired[User | UserDict]
