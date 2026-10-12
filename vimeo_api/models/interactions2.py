from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .add_privacy_user import AddPrivacyUser, AddPrivacyUserDict
from .block1 import Block1, Block1Dict
from .connected_apps1 import ConnectedApps1, ConnectedApps1Dict
from .follow2 import Follow2, Follow2Dict
from .report import Report, ReportDict


class Interactions2(SdkBaseModel):
    add_privacy_user: Optional[AddPrivacyUser] = UNSET
    block: Block1
    """Information about the block status of the authenticated user."""

    connected_apps: Optional[ConnectedApps1] = UNSET
    follow: Optional[Follow2] = UNSET
    """Information about the followed status of the authenticated user."""

    report: Report
    """Information about where and how to report the requested user."""


class Interactions2Dict(TypedDict):
    add_privacy_user: NotRequired[AddPrivacyUserDict]
    block: Block1Dict
    connected_apps: NotRequired[ConnectedApps1Dict]
    follow: NotRequired[Follow2Dict]
    report: ReportDict
