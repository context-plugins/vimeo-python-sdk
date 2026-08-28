from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.grant_type2 import GrantType2OrStr


class OauthAuthorizeVimeoOauth1Request(SdkBaseModel):
    grant_type: GrantType2OrStr
    """The grant type. The value of this field must be ``vimeo_oauth1``.

    Option descriptions:
     * ``vimeo_oauth1`` - The grant type is for the OAuth1 token."""

    token: str
    """The OAuth 1 token."""

    token_secret: str
    """The OAuth 1 token secret."""


class OauthAuthorizeVimeoOauth1RequestDict(TypedDict):
    grant_type: GrantType2OrStr
    token: str
    token_secret: str
