from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Role(str, Enum):
    """The untranslated role of the user who made the request.

    Option descriptions:
     * ``Admin`` - The team member has admin permissions. They can upload and edit videos for the entire team and
            perform team administration tasks.
     * ``Contributor`` - The team member has contributor permissions. They can upload and edit videos for the entire
            team but can’t perform team administration tasks.
     * ``Contributor Plus`` - The team member has contributor-plus permissions. They can upload and edit videos for the
            entire team and have additional sets of permissions but can't perform team administration tasks.
     * ``Owner`` - The team member has owner permissions.
     * ``Uploader`` - The team member has uploader permissions. They can upload videos for the entire team but can’t
            edit videos.
     * ``Viewer`` - The team member has viewer permissions. They can access team videos and specific team folders but
            can’t upload or edit videos."""

    ADMIN = "Admin"
    CONTRIBUTOR = "Contributor"
    CONTRIBUTOR_PLUS = "Contributor Plus"
    OWNER = "Owner"
    UPLOADER = "Uploader"
    VIEWER = "Viewer"

    __str__ = str.__str__


RoleOrStr: TypeAlias = Annotated[Role | str, open_enum_validator(Role)]
