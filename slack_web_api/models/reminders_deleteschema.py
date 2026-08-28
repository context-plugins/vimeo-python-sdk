from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class RemindersDeleteschema(SdkBaseModel):
    """Schema for successful response from reminders.delete method"""

    ok: Literal["True"] = "True"


class RemindersDeleteschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
