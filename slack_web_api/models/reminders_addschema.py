from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .objs_reminder import ObjsReminder, ObjsReminderDict


class RemindersAddschema(SdkBaseModel):
    """Schema for successful response from reminders.add method"""

    ok: Literal["True"] = "True"
    reminder: ObjsReminder


class RemindersAddschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
    reminder: ObjsReminder | ObjsReminderDict
