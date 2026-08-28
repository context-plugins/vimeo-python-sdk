from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Skill(SdkBaseModel):
    name: str
    """The skill's display name."""

    uri: str
    """The skill's canonical relative URI."""


class SkillDict(TypedDict):
    name: str
    uri: str
