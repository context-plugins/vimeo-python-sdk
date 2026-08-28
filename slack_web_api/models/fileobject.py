from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .reactionobject import Reactionobject, ReactionobjectDict
from .shares import Shares, SharesDict


class Fileobject(SdkBaseModel):
    channels: Optional[list[str]] = UNSET
    comments_count: Optional[int] = UNSET
    created: Optional[int] = UNSET
    date_delete: Optional[int] = UNSET
    display_as_bot: Optional[bool] = UNSET
    editable: Optional[bool] = UNSET
    editor: Optional[str] = UNSET
    external_id: Optional[str] = UNSET
    external_type: Optional[str] = UNSET
    external_url: Optional[str] = UNSET
    filetype: Optional[str] = UNSET
    groups: Optional[list[str]] = UNSET
    has_rich_preview: Optional[bool] = UNSET
    id: Optional[str] = UNSET
    image_exif_rotation: Optional[int] = UNSET
    ims: Optional[list[str]] = UNSET
    is_external: Optional[bool] = UNSET
    is_public: Optional[bool] = UNSET
    is_starred: Optional[bool] = UNSET
    is_tombstoned: Optional[bool] = UNSET
    last_editor: Optional[str] = UNSET
    mimetype: Optional[str] = UNSET
    mode: Optional[str] = UNSET
    name: Optional[str] = UNSET
    non_owner_editable: Optional[bool] = UNSET
    num_stars: Optional[int] = UNSET
    original_h: Optional[int] = UNSET
    original_w: Optional[int] = UNSET
    permalink: Optional[str] = UNSET
    permalink_public: Optional[str] = UNSET
    pinned_info: Optional[Any] = UNSET
    pinned_to: Optional[list[str]] = UNSET
    pretty_type: Optional[str] = UNSET
    preview: Optional[str] = UNSET
    public_url_shared: Optional[bool] = UNSET
    reactions: Optional[list[Reactionobject]] = UNSET
    shares: Optional[Shares] = UNSET
    size: Optional[int] = UNSET
    source_team: Optional[str] = UNSET
    state: Optional[str] = UNSET
    thumb_1024: Optional[str] = UNSET
    thumb_1024_h: Optional[int] = UNSET
    thumb_1024_w: Optional[int] = UNSET
    thumb_160: Optional[str] = UNSET
    thumb_360: Optional[str] = UNSET
    thumb_360_h: Optional[int] = UNSET
    thumb_360_w: Optional[int] = UNSET
    thumb_480: Optional[str] = UNSET
    thumb_480_h: Optional[int] = UNSET
    thumb_480_w: Optional[int] = UNSET
    thumb_64: Optional[str] = UNSET
    thumb_720: Optional[str] = UNSET
    thumb_720_h: Optional[int] = UNSET
    thumb_720_w: Optional[int] = UNSET
    thumb_80: Optional[str] = UNSET
    thumb_800: Optional[str] = UNSET
    thumb_800_h: Optional[int] = UNSET
    thumb_800_w: Optional[int] = UNSET
    thumb_960: Optional[str] = UNSET
    thumb_960_h: Optional[int] = UNSET
    thumb_960_w: Optional[int] = UNSET
    thumb_tiny: Optional[str] = UNSET
    timestamp: Optional[int] = UNSET
    title: Optional[str] = UNSET
    updated: Optional[int] = UNSET
    url_private: Optional[str] = UNSET
    url_private_download: Optional[str] = UNSET
    user: Optional[str] = UNSET
    user_team: Optional[str] = UNSET
    username: Optional[str] = UNSET


class FileobjectDict(TypedDict):
    channels: NotRequired[list[str]]
    comments_count: NotRequired[int]
    created: NotRequired[int]
    date_delete: NotRequired[int]
    display_as_bot: NotRequired[bool]
    editable: NotRequired[bool]
    editor: NotRequired[str]
    external_id: NotRequired[str]
    external_type: NotRequired[str]
    external_url: NotRequired[str]
    filetype: NotRequired[str]
    groups: NotRequired[list[str]]
    has_rich_preview: NotRequired[bool]
    id: NotRequired[str]
    image_exif_rotation: NotRequired[int]
    ims: NotRequired[list[str]]
    is_external: NotRequired[bool]
    is_public: NotRequired[bool]
    is_starred: NotRequired[bool]
    is_tombstoned: NotRequired[bool]
    last_editor: NotRequired[str]
    mimetype: NotRequired[str]
    mode: NotRequired[str]
    name: NotRequired[str]
    non_owner_editable: NotRequired[bool]
    num_stars: NotRequired[int]
    original_h: NotRequired[int]
    original_w: NotRequired[int]
    permalink: NotRequired[str]
    permalink_public: NotRequired[str]
    pinned_info: NotRequired[Any]
    pinned_to: NotRequired[list[str]]
    pretty_type: NotRequired[str]
    preview: NotRequired[str]
    public_url_shared: NotRequired[bool]
    reactions: NotRequired[list[Reactionobject | ReactionobjectDict]]
    shares: NotRequired[Shares | SharesDict]
    size: NotRequired[int]
    source_team: NotRequired[str]
    state: NotRequired[str]
    thumb_1024: NotRequired[str]
    thumb_1024_h: NotRequired[int]
    thumb_1024_w: NotRequired[int]
    thumb_160: NotRequired[str]
    thumb_360: NotRequired[str]
    thumb_360_h: NotRequired[int]
    thumb_360_w: NotRequired[int]
    thumb_480: NotRequired[str]
    thumb_480_h: NotRequired[int]
    thumb_480_w: NotRequired[int]
    thumb_64: NotRequired[str]
    thumb_720: NotRequired[str]
    thumb_720_h: NotRequired[int]
    thumb_720_w: NotRequired[int]
    thumb_80: NotRequired[str]
    thumb_800: NotRequired[str]
    thumb_800_h: NotRequired[int]
    thumb_800_w: NotRequired[int]
    thumb_960: NotRequired[str]
    thumb_960_h: NotRequired[int]
    thumb_960_w: NotRequired[int]
    thumb_tiny: NotRequired[str]
    timestamp: NotRequired[int]
    title: NotRequired[str]
    updated: NotRequired[int]
    url_private: NotRequired[str]
    url_private_download: NotRequired[str]
    user: NotRequired[str]
    user_team: NotRequired[str]
    username: NotRequired[str]
