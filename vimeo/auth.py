from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, TypeAlias

from .core import AsyncAuthScheme, AuthScheme


@dataclass(frozen=True, slots=True, kw_only=True)
class AuthSchemes:
    bearer: AuthScheme
    oauth2_authorization_code: AuthScheme
    oauth2_client_credentials: AuthScheme


@dataclass(frozen=True, slots=True, kw_only=True)
class AsyncAuthSchemes:
    bearer: AsyncAuthScheme
    oauth2_authorization_code: AsyncAuthScheme
    oauth2_client_credentials: AsyncAuthScheme


Oauth2AuthorizationCodeScope: TypeAlias = Literal[
    "ai",
    "create",
    "delete",
    "edit",
    "email",
    "interact",
    "private",
    "promo_codes",
    "public",
    "purchase",
    "purchased",
    "scim",
    "stats",
    "upload",
    "video_files",
]
"""``ai``: Access AI features including transcription and translation. ``create``: Create new albums, channels, and so
on. ``delete``: Delete videos, albums, channels, and so on. ``edit``: Edit existing videos, albums, channels, and so on.
``email``: Access to email addresses. ``interact``: Interact with Vimeo resources on a member's behalf, such as liking a
video or following another member. ``private``: Access private member data. ``promo_codes``: Add, remove, and review
Vimeo On Demand promotions. ``public``: Access public member data. ``purchase``: Purchase content. ``purchased``: Access
a member's Vimeo On Demand purchase history. ``scim``: Manage users and team groups via the SCIM protocol. ``stats``:
Access video stats. ``upload``: Upload videos. ``video_files``: Access video files belonging to members with a PRO
subscription or higher."""

Oauth2ClientCredentialsScope: TypeAlias = Literal[
    "ai",
    "create",
    "delete",
    "edit",
    "email",
    "interact",
    "private",
    "promo_codes",
    "public",
    "purchase",
    "purchased",
    "scim",
    "stats",
    "upload",
    "video_files",
]
"""``ai``: Access AI features including transcription and translation. ``create``: Create new albums, channels, and so
on. ``delete``: Delete videos, albums, channels, and so on. ``edit``: Edit existing videos, albums, channels, and so on.
``email``: Access to email addresses. ``interact``: Interact with Vimeo resources on a member's behalf, such as liking a
video or following another member. ``private``: Access private member data. ``promo_codes``: Add, remove, and review
Vimeo On Demand promotions. ``public``: Access public member data. ``purchase``: Purchase content. ``purchased``: Access
a member's Vimeo On Demand purchase history. ``scim``: Manage users and team groups via the SCIM protocol. ``stats``:
Access video stats. ``upload``: Upload videos. ``video_files``: Access video files belonging to members with a PRO
subscription or higher."""
