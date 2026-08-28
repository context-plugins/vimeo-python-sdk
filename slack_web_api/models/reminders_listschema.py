from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .objs_reminder import ObjsReminder, ObjsReminderDict


class RemindersListschema(SdkBaseModel):
    """Schema for successful response from reminders.list method"""

    ok: Literal["True"] = "True"
    reminders: list[ObjsReminder]


class RemindersListschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
    reminders: list[ObjsReminder | ObjsReminderDict]
