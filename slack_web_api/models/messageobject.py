from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .attachment import Attachment, AttachmentDict
from .block_kitblock import BlockKitblock, BlockKitblockDict
from .bot_profile_object import BotProfileObject, BotProfileObjectDict
from .file_comment_object import FileCommentObject, FileCommentObjectDict
from .fileobject import Fileobject, FileobjectDict
from .icons1 import Icons1, Icons1Dict
from .objs_user_profile_short import ObjsUserProfileShort, ObjsUserProfileShortDict
from .reactionobject import Reactionobject, ReactionobjectDict


class Messageobject(SdkBaseModel):
    attachments: Optional[list[Attachment]] = UNSET
    blocks: Optional[list[BlockKitblock]] = UNSET
    """This is a very loose definition, in the future, we'll populate this with deeper schema in this definition
    namespace."""

    bot_id: Optional[Any] = UNSET
    bot_profile: Optional[BotProfileObject] = UNSET
    client_msg_id: Optional[str] = UNSET
    comment: Optional[FileCommentObject] = UNSET
    display_as_bot: Optional[bool] = UNSET
    file: Optional[Fileobject] = UNSET
    files: Optional[list[Fileobject]] = UNSET
    icons: Optional[Icons1] = UNSET
    inviter: Optional[str] = UNSET
    is_delayed_message: Optional[bool] = UNSET
    is_intro: Optional[bool] = UNSET
    is_starred: Optional[bool] = UNSET
    last_read: Optional[str] = UNSET
    latest_reply: Optional[str] = UNSET
    name: Optional[str] = UNSET
    old_name: Optional[str] = UNSET
    parent_user_id: Optional[str] = UNSET
    permalink: Optional[str] = UNSET
    pinned_to: Optional[list[str]] = UNSET
    purpose: Optional[str] = UNSET
    reactions: Optional[list[Reactionobject]] = UNSET
    reply_count: Optional[int] = UNSET
    reply_users: Optional[list[str]] = UNSET
    reply_users_count: Optional[int] = UNSET
    source_team: Optional[str] = UNSET
    subscribed: Optional[bool] = UNSET
    subtype: Optional[str] = UNSET
    team: Optional[str] = UNSET
    text: str
    thread_ts: Optional[str] = UNSET
    topic: Optional[str] = UNSET
    ts: str
    type_: str = Field(alias="type")
    unread_count: Optional[int] = UNSET
    upload: Optional[bool] = UNSET
    user: Optional[str] = UNSET
    user_profile: Optional[ObjsUserProfileShort] = UNSET
    user_team: Optional[str] = UNSET
    username: Optional[str] = UNSET


class MessageobjectDict(TypedDict):
    attachments: NotRequired[list[Attachment | AttachmentDict]]
    blocks: NotRequired[list[BlockKitblock | BlockKitblockDict]]
    bot_id: NotRequired[Any]
    bot_profile: NotRequired[BotProfileObject | BotProfileObjectDict]
    client_msg_id: NotRequired[str]
    comment: NotRequired[FileCommentObject | FileCommentObjectDict]
    display_as_bot: NotRequired[bool]
    file: NotRequired[Fileobject | FileobjectDict]
    files: NotRequired[list[Fileobject | FileobjectDict]]
    icons: NotRequired[Icons1 | Icons1Dict]
    inviter: NotRequired[str]
    is_delayed_message: NotRequired[bool]
    is_intro: NotRequired[bool]
    is_starred: NotRequired[bool]
    last_read: NotRequired[str]
    latest_reply: NotRequired[str]
    name: NotRequired[str]
    old_name: NotRequired[str]
    parent_user_id: NotRequired[str]
    permalink: NotRequired[str]
    pinned_to: NotRequired[list[str]]
    purpose: NotRequired[str]
    reactions: NotRequired[list[Reactionobject | ReactionobjectDict]]
    reply_count: NotRequired[int]
    reply_users: NotRequired[list[str]]
    reply_users_count: NotRequired[int]
    source_team: NotRequired[str]
    subscribed: NotRequired[bool]
    subtype: NotRequired[str]
    team: NotRequired[str]
    text: str
    thread_ts: NotRequired[str]
    topic: NotRequired[str]
    ts: str
    type_: str
    unread_count: NotRequired[int]
    upload: NotRequired[bool]
    user: NotRequired[str]
    user_profile: NotRequired[ObjsUserProfileShort | ObjsUserProfileShortDict]
    user_team: NotRequired[str]
    username: NotRequired[str]
