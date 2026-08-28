from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, TypeAlias

from .core import AsyncAuthScheme, AuthScheme


@dataclass(frozen=True, slots=True, kw_only=True)
class AuthSchemes:
    slack_auth: AuthScheme


@dataclass(frozen=True, slots=True, kw_only=True)
class AsyncAuthSchemes:
    slack_auth: AsyncAuthScheme


SlackAuthScope: TypeAlias = Literal[
    "admin",
    "admin.apps:read",
    "admin.apps:write",
    "admin.conversations:read",
    "admin.conversations:write",
    "admin.invites:read",
    "admin.invites:write",
    "admin.teams:read",
    "admin.teams:write",
    "admin.usergroups:read",
    "admin.usergroups:write",
    "admin.users:read",
    "admin.users:write",
    "authorizations:read",
    "bot",
    "calls:read",
    "calls:write",
    "channels:history",
    "channels:manage",
    "channels:read",
    "channels:write",
    "chat:write",
    "chat:write:bot",
    "chat:write:user",
    "conversations:history",
    "conversations:read",
    "conversations:write",
    "dnd:read",
    "dnd:write",
    "emoji:read",
    "files:read",
    "files:write:user",
    "groups:history",
    "groups:read",
    "groups:write",
    "identity.basic",
    "im:history",
    "im:read",
    "im:write",
    "links:write",
    "mpim:history",
    "mpim:read",
    "mpim:write",
    "none",
    "pins:read",
    "pins:write",
    "reactions:read",
    "reactions:write",
    "reminders:read",
    "reminders:write",
    "remote_files:read",
    "remote_files:share",
    "remote_files:write",
    "rtm:stream",
    "search:read",
    "stars:read",
    "stars:write",
    "team:read",
    "tokens.basic",
    "usergroups:read",
    "usergroups:write",
    "users.profile:read",
    "users.profile:write",
    "users:read",
    "users:read.email",
    "users:write",
    "workflow.steps:execute",
]
"""``admin``: admin. ``admin.apps:read``: admin.apps:read. ``admin.apps:write``: admin.apps:write.
``admin.conversations:read``: admin.conversations:read. ``admin.conversations:write``: admin.conversations:write.
``admin.invites:read``: admin.invites:read. ``admin.invites:write``: admin.invites:write. ``admin.teams:read``:
admin.teams:read. ``admin.teams:write``: admin.teams:write. ``admin.usergroups:read``: admin.usergroups:read.
``admin.usergroups:write``: admin.usergroups:write. ``admin.users:read``: admin.users:read. ``admin.users:write``:
admin.users:write. ``authorizations:read``: authorizations:read. ``bot``: Bot user scope. ``calls:read``: calls:read.
``calls:write``: calls:write. ``channels:history``: channels:history. ``channels:manage``: channels:manage.
``channels:read``: channels:read. ``channels:write``: channels:write. ``chat:write``: chat:write. ``chat:write:bot``:
Author messages as a bot. ``chat:write:user``: Author messages as a user. ``conversations:history``:
conversations:history. ``conversations:read``: conversations:read. ``conversations:write``: conversations:write.
``dnd:read``: dnd:read. ``dnd:write``: dnd:write. ``emoji:read``: emoji:read. ``files:read``: files:read.
``files:write:user``: files:write:user. ``groups:history``: groups:history. ``groups:read``: groups:read.
``groups:write``: groups:write. ``identity.basic``: identity.basic. ``im:history``: im:history. ``im:read``: im:read.
``im:write``: im:write. ``links:write``: links:write. ``mpim:history``: mpim:history. ``mpim:read``: mpim:read.
``mpim:write``: mpim:write. ``none``: No scope required. ``pins:read``: pins:read. ``pins:write``: pins:write.
``reactions:read``: reactions:read. ``reactions:write``: reactions:write. ``reminders:read``: reminders:read.
``reminders:write``: reminders:write. ``remote_files:read``: remote_files:read. ``remote_files:share``:
remote_files:share. ``remote_files:write``: remote_files:write. ``rtm:stream``: rtm:stream. ``search:read``:
search:read. ``stars:read``: stars:read. ``stars:write``: stars:write. ``team:read``: team:read. ``tokens.basic``:
tokens.basic. ``usergroups:read``: usergroups:read. ``usergroups:write``: usergroups:write. ``users.profile:read``:
users.profile:read. ``users.profile:write``: users.profile:write. ``users:read``: users:read. ``users:read.email``:
users:read.email. ``users:write``: users:write. ``workflow.steps:execute``: workflow.steps:execute."""
