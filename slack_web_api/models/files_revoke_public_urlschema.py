from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .fileobject import Fileobject, FileobjectDict


class FilesRevokePublicUrlschema(SdkBaseModel):
    """Schema for successful response from files.revokePublicURL method"""

    file: Fileobject
    ok: Literal["True"] = "True"


class FilesRevokePublicUrlschemaDict(TypedDict):
    file: Fileobject | FileobjectDict
    ok: NotRequired[Literal["True"]]
