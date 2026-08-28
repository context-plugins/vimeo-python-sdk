from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class RemindersCompleteschema(SdkBaseModel):
    """Schema for successful response from reminders.complete method"""

    ok: Literal["True"] = "True"


class RemindersCompleteschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
