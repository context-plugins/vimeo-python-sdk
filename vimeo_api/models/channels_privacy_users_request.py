from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ChannelsPrivacyUsersRequest(SdkBaseModel):
    users: list[str]
    """The array of either the user URIs or the user IDs to permit to access the private channel."""


class ChannelsPrivacyUsersRequestDict(TypedDict):
    users: list[str]
