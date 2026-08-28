from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .current import Current, CurrentDict


class ExternalOrgMigrations(SdkBaseModel):
    current: list[Current]
    date_updated: int


class ExternalOrgMigrationsDict(TypedDict):
    current: list[Current | CurrentDict]
    date_updated: int
