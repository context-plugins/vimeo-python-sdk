from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .objs_reminder import ObjsReminder, ObjsReminderDict


class RemindersInfoschema(SdkBaseModel):
    """Schema for successful response from reminders.info method"""

    ok: Literal["True"] = "True"
    reminder: ObjsReminder


class RemindersInfoschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
    reminder: ObjsReminder | ObjsReminderDict
