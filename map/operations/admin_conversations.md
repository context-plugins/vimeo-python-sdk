<!-- Generated file — do not edit; regenerated with the SDK. -->

# AdminConversations — operations

Accessor: `client.admin_conversations` · Source: `slack_web_api/apis/admin_conversations.py` · 13 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.admin_conversations.admin_conversations_archive

- **Route**: `POST /admin.conversations.archive`
- **Signature**: `def admin_conversations_archive(token: str, content_type: ContentTypeOrStr, channel_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `channel_id`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `channel_id` — form field
- **Returns (parsed)**: `AdminConversationsArchiveschema`
- **Returns (raw)**: `ApiResult[AdminConversationsArchiveschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `AdminConversationsArchiveschema` | `slack_web_api/models/admin_conversations_archiveschema.py` |

### client.admin_conversations.admin_conversations_convert_to_private

- **Route**: `POST /admin.conversations.convertToPrivate`
- **Signature**: `def admin_conversations_convert_to_private(token: str, content_type: ContentTypeOrStr, channel_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `channel_id`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `channel_id` — form field
- **Returns (parsed)**: `AdminConversationsConvertToPrivateschema`
- **Returns (raw)**: `ApiResult[AdminConversationsConvertToPrivateschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `AdminConversationsConvertToPrivateschema` | `slack_web_api/models/admin_conversations_convert_to_privateschema.py` |

### client.admin_conversations.admin_conversations_create

- **Route**: `POST /admin.conversations.create`
- **Signature**: `def admin_conversations_create(token: str, content_type: ContentTypeOrStr, name: str, is_private: bool, *, description: str | None = None, org_wide: bool | None = None, team_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `name`, `is_private`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `name` — form field · `is_private` — form field · `description` — form field · `org_wide` — form field · `team_id` — form field
- **Returns (parsed)**: `AdminConversationsCreateschema`
- **Returns (raw)**: `ApiResult[AdminConversationsCreateschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `AdminConversationsCreateschema` | `slack_web_api/models/admin_conversations_createschema.py` |

### client.admin_conversations.admin_conversations_delete

- **Route**: `POST /admin.conversations.delete`
- **Signature**: `def admin_conversations_delete(token: str, content_type: ContentTypeOrStr, channel_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `channel_id`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `channel_id` — form field
- **Returns (parsed)**: `AdminConversationsDeleteschema`
- **Returns (raw)**: `ApiResult[AdminConversationsDeleteschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `AdminConversationsDeleteschema` | `slack_web_api/models/admin_conversations_deleteschema.py` |

### client.admin_conversations.admin_conversations_disconnect_shared

- **Route**: `POST /admin.conversations.disconnectShared`
- **Signature**: `def admin_conversations_disconnect_shared(token: str, content_type: ContentTypeOrStr, channel_id: str, *, leaving_team_ids: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `channel_id`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `channel_id` — form field · `leaving_team_ids` — form field
- **Returns (parsed)**: `AdminConversationsRenameschema`
- **Returns (raw)**: `ApiResult[AdminConversationsRenameschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `AdminConversationsRenameschema` | `slack_web_api/models/admin_conversations_renameschema.py` |

### client.admin_conversations.admin_conversations_get_conversation_prefs

- **Route**: `GET /admin.conversations.getConversationPrefs`
- **Signature**: `def admin_conversations_get_conversation_prefs(channel_id: str, token: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel_id`, `token`, `content_type`
- **Params**: `channel_id` — query · `token` — header · `content_type` — header `Content-Type`
- **Returns (parsed)**: `AdminConversationsGetConversationPrefsschema`
- **Returns (raw)**: `ApiResult[AdminConversationsGetConversationPrefsschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `AdminConversationsGetConversationPrefsschema` | `slack_web_api/models/admin_conversations_get_conversation_prefsschema.py` |

### client.admin_conversations.admin_conversations_get_teams

- **Route**: `GET /admin.conversations.getTeams`
- **Signature**: `def admin_conversations_get_teams(channel_id: str, token: str, content_type: ContentTypeOrStr, *, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel_id`, `token`, `content_type`
- **Params**: `channel_id` — query · `cursor` — query · `limit` — query · `token` — header · `content_type` — header `Content-Type`
- **Returns (parsed)**: `AdminConversationsGetTeamsschema`
- **Returns (raw)**: `ApiResult[AdminConversationsGetTeamsschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `AdminConversationsGetTeamsschema` | `slack_web_api/models/admin_conversations_get_teamsschema.py` |

### client.admin_conversations.admin_conversations_invite

- **Route**: `POST /admin.conversations.invite`
- **Signature**: `def admin_conversations_invite(token: str, content_type: ContentTypeOrStr, user_ids: str, channel_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `user_ids`, `channel_id`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `user_ids` — form field · `channel_id` — form field
- **Returns (parsed)**: `AdminConversationsInviteschema`
- **Returns (raw)**: `ApiResult[AdminConversationsInviteschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `AdminConversationsInviteschema` | `slack_web_api/models/admin_conversations_inviteschema.py` |

### client.admin_conversations.admin_conversations_rename

- **Route**: `POST /admin.conversations.rename`
- **Signature**: `def admin_conversations_rename(token: str, content_type: ContentTypeOrStr, channel_id: str, name: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `channel_id`, `name`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `channel_id` — form field · `name` — form field
- **Returns (parsed)**: `AdminConversationsRenameschema1`
- **Returns (raw)**: `ApiResult[AdminConversationsRenameschema1, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `AdminConversationsRenameschema1` | `slack_web_api/models/admin_conversations_renameschema1.py` |

### client.admin_conversations.admin_conversations_search

- **Route**: `GET /admin.conversations.search`
- **Signature**: `def admin_conversations_search(token: str, content_type: ContentTypeOrStr, *, team_ids: str | None = None, query: str | None = None, limit: int | None = None, cursor: str | None = None, search_channel_types: str | None = None, sort: str | None = None, sort_dir: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`
- **Params**: `team_ids` — query · `query` — query · `limit` — query · `cursor` — query · `search_channel_types` — query · `sort` — query · `sort_dir` — query · `token` — header · `content_type` — header `Content-Type`
- **Returns (parsed)**: `AdminConversationsSearchschema`
- **Returns (raw)**: `ApiResult[AdminConversationsSearchschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `AdminConversationsSearchschema` | `slack_web_api/models/admin_conversations_searchschema.py` |

### client.admin_conversations.admin_conversations_set_conversation_prefs

- **Route**: `POST /admin.conversations.setConversationPrefs`
- **Signature**: `def admin_conversations_set_conversation_prefs(token: str, content_type: ContentTypeOrStr, channel_id: str, prefs: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `channel_id`, `prefs`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `channel_id` — form field · `prefs` — form field
- **Returns (parsed)**: `AdminConversationsSetConversationPrefsschema`
- **Returns (raw)**: `ApiResult[AdminConversationsSetConversationPrefsschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `AdminConversationsSetConversationPrefsschema` | `slack_web_api/models/admin_conversations_set_conversation_prefsschema.py` |

### client.admin_conversations.admin_conversations_set_teams

- **Route**: `POST /admin.conversations.setTeams`
- **Signature**: `def admin_conversations_set_teams(token: str, content_type: ContentTypeOrStr, channel_id: str, *, team_id: str | None = None, target_team_ids: str | None = None, org_channel: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `channel_id`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `channel_id` — form field · `team_id` — form field · `target_team_ids` — form field · `org_channel` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin_conversations.admin_conversations_unarchive

- **Route**: `POST /admin.conversations.unarchive`
- **Signature**: `def admin_conversations_unarchive(token: str, content_type: ContentTypeOrStr, channel_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `channel_id`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `channel_id` — form field
- **Returns (parsed)**: `AdminConversationsUnarchiveschema`
- **Returns (raw)**: `ApiResult[AdminConversationsUnarchiveschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `AdminConversationsUnarchiveschema` | `slack_web_api/models/admin_conversations_unarchiveschema.py` |

