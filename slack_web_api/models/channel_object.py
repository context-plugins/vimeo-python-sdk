from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .purpose import Purpose, PurposeDict
from .topic import Topic, TopicDict


class ChannelObject(SdkBaseModel):
    accepted_user: Optional[str] = UNSET
    created: int
    creator: str
    id: str
    is_archived: Optional[bool] = UNSET
    is_channel: bool
    is_frozen: Optional[bool] = UNSET
    is_general: Optional[bool] = UNSET
    is_member: Optional[bool] = UNSET
    is_moved: Optional[int] = UNSET
    is_mpim: bool
    is_non_threadable: Optional[bool] = UNSET
    is_org_shared: bool
    is_pending_ext_shared: Optional[bool] = UNSET
    is_private: bool
    is_read_only: Optional[bool] = UNSET
    is_shared: bool
    is_thread_only: Optional[bool] = UNSET
    last_read: Optional[str] = UNSET
    latest: Optional[Any] = UNSET
    members: list[str]
    name: str
    name_normalized: str
    num_members: Optional[int] = UNSET
    pending_shared: Optional[list[str]] = UNSET
    previous_names: Optional[list[str]] = UNSET
    priority: Optional[float] = UNSET
    purpose: Purpose
    topic: Topic
    unlinked: Optional[int] = UNSET
    unread_count: Optional[int] = UNSET
    unread_count_display: Optional[int] = UNSET


class ChannelObjectDict(TypedDict):
    accepted_user: NotRequired[str]
    created: int
    creator: str
    id: str
    is_archived: NotRequired[bool]
    is_channel: bool
    is_frozen: NotRequired[bool]
    is_general: NotRequired[bool]
    is_member: NotRequired[bool]
    is_moved: NotRequired[int]
    is_mpim: bool
    is_non_threadable: NotRequired[bool]
    is_org_shared: bool
    is_pending_ext_shared: NotRequired[bool]
    is_private: bool
    is_read_only: NotRequired[bool]
    is_shared: bool
    is_thread_only: NotRequired[bool]
    last_read: NotRequired[str]
    latest: NotRequired[Any]
    members: list[str]
    name: str
    name_normalized: str
    num_members: NotRequired[int]
    pending_shared: NotRequired[list[str]]
    previous_names: NotRequired[list[str]]
    priority: NotRequired[float]
    purpose: Purpose | PurposeDict
    topic: Topic | TopicDict
    unlinked: NotRequired[int]
    unread_count: NotRequired[int]
    unread_count_display: NotRequired[int]
