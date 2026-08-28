from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Userprofileobject(SdkBaseModel):
    always_active: Optional[bool] = UNSET
    api_app_id: Optional[str] = UNSET
    avatar_hash: str
    bot_id: Optional[str] = UNSET
    display_name: str
    display_name_normalized: str
    email: OptionalNullable[str] = UNSET
    fields: list[Any | None]
    first_name: OptionalNullable[str] = UNSET
    guest_expiration_ts: OptionalNullable[int] = UNSET
    guest_invited_by: OptionalNullable[str] = UNSET
    image_1024: OptionalNullable[str] = UNSET
    image_192: OptionalNullable[str] = UNSET
    image_24: OptionalNullable[str] = UNSET
    image_32: OptionalNullable[str] = UNSET
    image_48: OptionalNullable[str] = UNSET
    image_512: OptionalNullable[str] = UNSET
    image_72: OptionalNullable[str] = UNSET
    image_original: OptionalNullable[str] = UNSET
    is_app_user: Optional[bool] = UNSET
    is_custom_image: Optional[bool] = UNSET
    is_restricted: OptionalNullable[bool] = UNSET
    is_ultra_restricted: OptionalNullable[bool] = UNSET
    last_avatar_image_hash: Optional[str] = UNSET
    last_name: OptionalNullable[str] = UNSET
    memberships_count: Optional[int] = UNSET
    name: OptionalNullable[str] = UNSET
    phone: str
    pronouns: Optional[str] = UNSET
    real_name: str
    real_name_normalized: str
    skype: str
    status_default_emoji: Optional[str] = UNSET
    status_default_text: Optional[str] = UNSET
    status_default_text_canonical: OptionalNullable[str] = UNSET
    status_emoji: str
    status_expiration: Optional[int] = UNSET
    status_text: str
    status_text_canonical: OptionalNullable[str] = UNSET
    team: Optional[str] = UNSET
    title: str
    updated: Optional[int] = UNSET
    user_id: Optional[str] = UNSET
    username: OptionalNullable[str] = UNSET


class UserprofileobjectDict(TypedDict):
    always_active: NotRequired[bool]
    api_app_id: NotRequired[str]
    avatar_hash: str
    bot_id: NotRequired[str]
    display_name: str
    display_name_normalized: str
    email: NotRequired[str | None]
    fields: list[Any | None]
    first_name: NotRequired[str | None]
    guest_expiration_ts: NotRequired[int | None]
    guest_invited_by: NotRequired[str | None]
    image_1024: NotRequired[str | None]
    image_192: NotRequired[str | None]
    image_24: NotRequired[str | None]
    image_32: NotRequired[str | None]
    image_48: NotRequired[str | None]
    image_512: NotRequired[str | None]
    image_72: NotRequired[str | None]
    image_original: NotRequired[str | None]
    is_app_user: NotRequired[bool]
    is_custom_image: NotRequired[bool]
    is_restricted: NotRequired[bool | None]
    is_ultra_restricted: NotRequired[bool | None]
    last_avatar_image_hash: NotRequired[str]
    last_name: NotRequired[str | None]
    memberships_count: NotRequired[int]
    name: NotRequired[str | None]
    phone: str
    pronouns: NotRequired[str]
    real_name: str
    real_name_normalized: str
    skype: str
    status_default_emoji: NotRequired[str]
    status_default_text: NotRequired[str]
    status_default_text_canonical: NotRequired[str | None]
    status_emoji: str
    status_expiration: NotRequired[int]
    status_text: str
    status_text_canonical: NotRequired[str | None]
    team: NotRequired[str]
    title: str
    updated: NotRequired[int]
    user_id: NotRequired[str]
    username: NotRequired[str | None]
