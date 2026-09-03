from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class OauthAuthorizeClientRequest(SdkBaseModel):
    grant_type: Literal["client_credentials"] = "client_credentials"
    """The grant type. The value of this field must be ``client_credentials``.

    Option descriptions:
     * ``client_credentials`` - The grant type is for the client credentials."""

    scope: str
    """A space-separated list of the authentication scopes to access. The default is ``public``."""


class OauthAuthorizeClientRequestDict(TypedDict):
    grant_type: NotRequired[Literal["client_credentials"]]
    scope: str
