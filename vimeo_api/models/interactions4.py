from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .add_subfolder import AddSubfolder, AddSubfolderDict
from .delete1 import Delete1, Delete1Dict
from .delete_video import DeleteVideo, DeleteVideoDict
from .edit1 import Edit1, Edit1Dict
from .edit_settings import EditSettings, EditSettingsDict
from .invite1 import Invite1, Invite1Dict
from .move_video import MoveVideo, MoveVideoDict
from .upload_video import UploadVideo, UploadVideoDict
from .view2 import View2, View2Dict


class Interactions4(SdkBaseModel):
    """A list of permitted interactions related to the folder."""

    add_subfolder: AddSubfolder
    """Information about adding a subfolder to the current folder."""

    allow_multiple_review_links: Optional[bool] = UNSET
    """Whether the folder can have multiple review links."""

    can_comment: Optional[bool] = UNSET
    """Whether the user can comment on the videos of the current folder."""

    delete: Delete1
    """The user's delete permissions information for this project."""

    delete_video: DeleteVideo
    """The user's delete permissions information for this project."""

    edit: Edit1
    """The user's edit permissions information for this project."""

    edit_settings: EditSettings
    """The user's edit settings permissions information for this project."""

    invite: Invite1
    """The user's invite permissions information for this project."""

    move_video: MoveVideo
    """The user's move permissions information for this project."""

    review_redirect_link: Optional[str] = UNSET
    """The default review redirect link for the current folder."""

    upload_video: UploadVideo
    """The user's upload permissions information for this project."""

    view: View2
    """The user's view permissions information for this project."""


class Interactions4Dict(TypedDict):
    add_subfolder: AddSubfolderDict
    allow_multiple_review_links: NotRequired[bool]
    can_comment: NotRequired[bool]
    delete: Delete1Dict
    delete_video: DeleteVideoDict
    edit: Edit1Dict
    edit_settings: EditSettingsDict
    invite: Invite1Dict
    move_video: MoveVideoDict
    review_redirect_link: NotRequired[str]
    upload_video: UploadVideoDict
    view: View2Dict
