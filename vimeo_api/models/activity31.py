from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .category import Category, CategoryDict
from .channel import Channel, ChannelDict
from .enums.type10 import Type10OrStr
from .group import Group, GroupDict
from .metadata7 import Metadata7, Metadata7Dict
from .on_demand_page import OnDemandPage, OnDemandPageDict
from .tag_model import TagModel, TagModelDict
from .user import User, UserDict
from .video import Video, VideoDict


class Activity31(SdkBaseModel):
    category: Optional[Category] = UNSET
    """The category associated with the event. This field is present only when the activity type is ``category``."""

    channel: Optional[Channel] = UNSET
    """The channel associated with the event. This field is present only when the activity type is ``channel``."""

    clip: Video
    """The video associated with the activity."""

    group: Optional[Group] = UNSET
    """The group associated with the event. This field is present only when the activity type is ``group``."""

    metadata: Metadata7
    """Information about the activity's metadata."""

    ondemand_page: Optional[OnDemandPage] = UNSET
    """The Vimeo On Demand page associated with the event. This field is present only when the activity type is
    ``ondemand``."""

    tag: Optional[TagModel] = UNSET
    """The tag associated with the event. This field is present only when the activity type is ``tag``."""

    time: str
    """The time that the event occurred."""

    type_: Type10OrStr = Field(alias="type")
    """The activity type.

    Option descriptions:
     * ``appearance`` - The activity is an appearance action.
     * ``category`` - The activity is a category action.
     * ``channel`` - The activity is a channel action.
     * ``facebook_feed`` - The activity is a Facebook feed action.
     * ``group`` - The activity is a group action.
     * ``like`` - The activity is a like action.
     * ``ondemand`` - The activity is a Vimeo On Demand action.
     * ``share`` - The activity is a share action.
     * ``tag`` - The activity is a tag action.
     * ``twitter_timeline`` - The activity is a Twitter timeline action.
     * ``upload`` - The activity is an upload action."""

    user: Optional[User] = UNSET
    """The user associated with the event. This field is present only when the activity type is ``like``,
    ``appearance``, or ``share``."""


class Activity31Dict(TypedDict):
    category: NotRequired[CategoryDict]
    channel: NotRequired[ChannelDict]
    clip: VideoDict
    group: NotRequired[GroupDict]
    metadata: Metadata7Dict
    ondemand_page: NotRequired[OnDemandPageDict]
    tag: NotRequired[TagModelDict]
    time: str
    type_: Type10OrStr
    user: NotRequired[UserDict]
