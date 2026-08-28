from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Kind(str, Enum):
    """The node kind.

    Option descriptions:
     * ``category`` - A grouping node; its children reference it via ``parent_id``.
     * ``external`` - Handed off to a dedicated form (see ``external_url``), not POST-able here.
     * ``reason`` - A submittable leaf; its ``id`` is the opaque reason UUID to POST."""

    CATEGORY = "category"
    EXTERNAL = "external"
    REASON = "reason"

    __str__ = str.__str__


KindOrStr: TypeAlias = Annotated[Kind | str, open_enum_validator(Kind)]
