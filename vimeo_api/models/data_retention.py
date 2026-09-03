from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .policy import Policy, PolicyDict


class DataRetention(SdkBaseModel):
    policy: Policy
    """Information about the folder's data retention policy. This data requires a bearer token with the ``private``
    scope."""


class DataRetentionDict(TypedDict):
    policy: Policy | PolicyDict
