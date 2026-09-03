from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .folder_uri import FolderUri, FolderUriDict
from .status2 import Status2, Status2Dict
from .upgrade_to_role import UpgradeToRole, UpgradeToRoleDict


class Properties(SdkBaseModel):
    """An object of suggested fields to be used for this interaction."""

    folder_uri: FolderUri
    """An object containing data on the value of **folder_uri** and whether it's required for the interaction."""

    status: Status2
    """An object containing data on the value of **status** and whether it's required for the interaction."""

    upgrade_to_role: UpgradeToRole
    """An object containing data on the value of **upgrade_to_role** and whether it's required for the interaction."""


class PropertiesDict(TypedDict):
    folder_uri: FolderUri | FolderUriDict
    status: Status2 | Status2Dict
    upgrade_to_role: UpgradeToRole | UpgradeToRoleDict
