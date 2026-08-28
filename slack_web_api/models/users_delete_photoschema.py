from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class UsersDeletePhotoschema(SdkBaseModel):
    """Schema for successful response from users.deletePhoto method"""

    ok: Literal["True"] = "True"


class UsersDeletePhotoschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
