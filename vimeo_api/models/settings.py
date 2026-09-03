from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Settings(SdkBaseModel):
    """The settings of the folder."""

    color: str
    """The hexadecimal color code of the folder color."""

    embed_preset_id: float | None
    """The ID of the embed preset for the folder."""

    folder_uri: str | None
    """The URI of the folder."""

    is_embed_preset_inheritance_enabled: Optional[bool] = UNSET
    """Whether embed preset inheritance is enabled for the folder."""


class SettingsDict(TypedDict):
    color: str
    embed_preset_id: float | None
    folder_uri: str | None
    is_embed_preset_inheritance_enabled: NotRequired[bool]
