from __future__ import annotations

from typing import Any, TypeAlias

from ..end_screen import EndScreen, EndScreenDict

EndScreen3: TypeAlias = EndScreen | list[Any]
"""A collection of information about the embeddable player's end screen. The API returns an empty array instead of an
object when no end screen is configured for the video."""

EndScreen3Dict: TypeAlias = EndScreenDict | list[Any]
