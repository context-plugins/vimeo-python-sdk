from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Profile1(SdkBaseModel):
    avatar_hash: str
    image_1024: str
    image_192: str
    image_24: str
    image_32: str
    image_48: str
    image_512: str
    image_72: str
    image_original: str


class Profile1Dict(TypedDict):
    avatar_hash: str
    image_1024: str
    image_192: str
    image_24: str
    image_32: str
    image_48: str
    image_512: str
    image_72: str
    image_original: str
