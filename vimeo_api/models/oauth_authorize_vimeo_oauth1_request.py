from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class OauthAuthorizeVimeoOauth1Request(SdkBaseModel):
    grant_type: Literal["vimeo_oauth1"] = "vimeo_oauth1"
    """The grant type. The value of this field must be ``vimeo_oauth1``.

    Option descriptions:
     * ``vimeo_oauth1`` - The grant type is for the OAuth1 token."""

    token: str
    """The OAuth 1 token."""

    token_secret: str
    """The OAuth 1 token secret."""


class OauthAuthorizeVimeoOauth1RequestDict(TypedDict):
    grant_type: NotRequired[Literal["vimeo_oauth1"]]
    token: str
    token_secret: str
