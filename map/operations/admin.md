<!-- Generated file — do not edit; regenerated with the SDK. -->

# Admin — operations

Accessor: `client.admin` · Source: `slack_web_api/apis/admin.py` · 56 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.admin.admin_apps_approve

- **Route**: `POST /admin.apps.approve`
- **Signature**: `def admin_apps_approve(token: str, content_type: ContentTypeOrStr, *, app_id: str | None = None, request_id: str | None = None, team_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `app_id` — form field · `request_id` — form field · `team_id` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin.admin_apps_approved_list

- **Route**: `GET /admin.apps.approved.list`
- **Signature**: `def admin_apps_approved_list(token: str, content_type: ContentTypeOrStr, *, limit: int | None = None, cursor: str | None = None, team_id: str | None = None, enterprise_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`
- **Params**: `token` — query · `limit` — query · `cursor` — query · `team_id` — query · `enterprise_id` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin.admin_apps_requests_list

- **Route**: `GET /admin.apps.requests.list`
- **Signature**: `def admin_apps_requests_list(token: str, content_type: ContentTypeOrStr, *, limit: int | None = None, cursor: str | None = None, team_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`
- **Params**: `token` — query · `limit` — query · `cursor` — query · `team_id` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin.admin_apps_restrict

- **Route**: `POST /admin.apps.restrict`
- **Signature**: `def admin_apps_restrict(token: str, content_type: ContentTypeOrStr, *, app_id: str | None = None, request_id: str | None = None, team_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `app_id` — form field · `request_id` — form field · `team_id` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin.admin_apps_restricted_list

- **Route**: `GET /admin.apps.restricted.list`
- **Signature**: `def admin_apps_restricted_list(token: str, content_type: ContentTypeOrStr, *, limit: int | None = None, cursor: str | None = None, team_id: str | None = None, enterprise_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`
- **Params**: `token` — query · `limit` — query · `cursor` — query · `team_id` — query · `enterprise_id` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin.admin_conversations_archive

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

### client.admin.admin_conversations_convert_to_private

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

### client.admin.admin_conversations_create

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

### client.admin.admin_conversations_delete

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

### client.admin.admin_conversations_disconnect_shared

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

### client.admin.admin_conversations_ekm_list_original_connected_channel_info

- **Route**: `GET /admin.conversations.ekm.listOriginalConnectedChannelInfo`
- **Signature**: `def admin_conversations_ekm_list_original_connected_channel_info(token: str, content_type: ContentTypeOrStr, *, channel_ids: str | None = None, team_ids: str | None = None, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`
- **Params**: `token` — query · `channel_ids` — query · `team_ids` — query · `limit` — query · `cursor` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin.admin_conversations_get_conversation_prefs

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

### client.admin.admin_conversations_get_teams

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

### client.admin.admin_conversations_invite

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

### client.admin.admin_conversations_rename

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

### client.admin.admin_conversations_restrict_access_add_group

- **Route**: `POST /admin.conversations.restrictAccess.addGroup`
- **Signature**: `def admin_conversations_restrict_access_add_group(content_type: ContentTypeOrStr, token: str, group_id: str, channel_id: str, *, team_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`, `token`, `group_id`, `channel_id`
- **Params**: `content_type` — header `Content-Type` · `token` — form field · `group_id` — form field · `channel_id` — form field · `team_id` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin.admin_conversations_restrict_access_list_groups

- **Route**: `GET /admin.conversations.restrictAccess.listGroups`
- **Signature**: `def admin_conversations_restrict_access_list_groups(token: str, channel_id: str, content_type: ContentTypeOrStr, *, team_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `channel_id`, `content_type`
- **Params**: `token` — query · `channel_id` — query · `team_id` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin.admin_conversations_restrict_access_remove_group

- **Route**: `POST /admin.conversations.restrictAccess.removeGroup`
- **Signature**: `def admin_conversations_restrict_access_remove_group(content_type: ContentTypeOrStr, token: str, team_id: str, group_id: str, channel_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`, `token`, `team_id`, `group_id`, `channel_id`
- **Params**: `content_type` — header `Content-Type` · `token` — form field · `team_id` — form field · `group_id` — form field · `channel_id` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin.admin_conversations_search

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

### client.admin.admin_conversations_set_conversation_prefs

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

### client.admin.admin_conversations_set_teams

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

### client.admin.admin_conversations_unarchive

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

### client.admin.admin_emoji_add

- **Route**: `POST /admin.emoji.add`
- **Signature**: `def admin_emoji_add(content_type: ContentTypeOrStr, token: str, name: str, url: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`, `token`, `name`, `url`
- **Params**: `content_type` — header `Content-Type` · `token` — form field · `name` — form field · `url` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin.admin_emoji_add_alias

- **Route**: `POST /admin.emoji.addAlias`
- **Signature**: `def admin_emoji_add_alias(content_type: ContentTypeOrStr, token: str, name: str, alias_for: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`, `token`, `name`, `alias_for`
- **Params**: `content_type` — header `Content-Type` · `token` — form field · `name` — form field · `alias_for` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin.admin_emoji_list

- **Route**: `GET /admin.emoji.list`
- **Signature**: `def admin_emoji_list(token: str, content_type: ContentTypeOrStr, *, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`
- **Params**: `token` — query · `cursor` — query · `limit` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin.admin_emoji_remove

- **Route**: `POST /admin.emoji.remove`
- **Signature**: `def admin_emoji_remove(content_type: ContentTypeOrStr, token: str, name: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`, `token`, `name`
- **Params**: `content_type` — header `Content-Type` · `token` — form field · `name` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin.admin_emoji_rename

- **Route**: `POST /admin.emoji.rename`
- **Signature**: `def admin_emoji_rename(content_type: ContentTypeOrStr, token: str, name: str, new_name: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`, `token`, `name`, `new_name`
- **Params**: `content_type` — header `Content-Type` · `token` — form field · `name` — form field · `new_name` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin.admin_invite_requests_approve

- **Route**: `POST /admin.inviteRequests.approve`
- **Signature**: `def admin_invite_requests_approve(token: str, content_type: ContentTypeOrStr, invite_request_id: str, *, team_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `invite_request_id`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `invite_request_id` — form field · `team_id` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin.admin_invite_requests_approved_list

- **Route**: `GET /admin.inviteRequests.approved.list`
- **Signature**: `def admin_invite_requests_approved_list(token: str, content_type: ContentTypeOrStr, *, team_id: str | None = None, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`
- **Params**: `team_id` — query · `cursor` — query · `limit` — query · `token` — header · `content_type` — header `Content-Type`
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin.admin_invite_requests_denied_list

- **Route**: `GET /admin.inviteRequests.denied.list`
- **Signature**: `def admin_invite_requests_denied_list(token: str, content_type: ContentTypeOrStr, *, team_id: str | None = None, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`
- **Params**: `team_id` — query · `cursor` — query · `limit` — query · `token` — header · `content_type` — header `Content-Type`
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin.admin_invite_requests_deny

- **Route**: `POST /admin.inviteRequests.deny`
- **Signature**: `def admin_invite_requests_deny(token: str, content_type: ContentTypeOrStr, invite_request_id: str, *, team_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `invite_request_id`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `invite_request_id` — form field · `team_id` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin.admin_invite_requests_list

- **Route**: `GET /admin.inviteRequests.list`
- **Signature**: `def admin_invite_requests_list(token: str, content_type: ContentTypeOrStr, *, team_id: str | None = None, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`
- **Params**: `team_id` — query · `cursor` — query · `limit` — query · `token` — header · `content_type` — header `Content-Type`
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin.admin_teams_admins_list

- **Route**: `GET /admin.teams.admins.list`
- **Signature**: `def admin_teams_admins_list(token: str, team_id: str, content_type: ContentTypeOrStr, *, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `team_id`, `content_type`
- **Params**: `token` — query · `team_id` — query · `limit` — query · `cursor` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin.admin_teams_create

- **Route**: `POST /admin.teams.create`
- **Signature**: `def admin_teams_create(token: str, content_type: ContentTypeOrStr, team_domain: str, team_name: str, *, team_description: str | None = None, team_discoverability: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `team_domain`, `team_name`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `team_domain` — form field · `team_name` — form field · `team_description` — form field · `team_discoverability` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin.admin_teams_list

- **Route**: `GET /admin.teams.list`
- **Signature**: `def admin_teams_list(token: str, content_type: ContentTypeOrStr, *, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`
- **Params**: `limit` — query · `cursor` — query · `token` — header · `content_type` — header `Content-Type`
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin.admin_teams_owners_list

- **Route**: `GET /admin.teams.owners.list`
- **Signature**: `def admin_teams_owners_list(token: str, team_id: str, content_type: ContentTypeOrStr, *, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `team_id`, `content_type`
- **Params**: `token` — query · `team_id` — query · `limit` — query · `cursor` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin.admin_teams_settings_info

- **Route**: `GET /admin.teams.settings.info`
- **Signature**: `def admin_teams_settings_info(team_id: str, token: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `team_id`, `token`, `content_type`
- **Params**: `team_id` — query · `token` — header · `content_type` — header `Content-Type`
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin.admin_teams_settings_set_default_channels

- **Route**: `POST /admin.teams.settings.setDefaultChannels`
- **Signature**: `def admin_teams_settings_set_default_channels(content_type: ContentTypeOrStr, token: str, team_id: str, channel_ids: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`, `token`, `team_id`, `channel_ids`
- **Params**: `content_type` — header `Content-Type` · `token` — form field · `team_id` — form field · `channel_ids` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin.admin_teams_settings_set_description

- **Route**: `POST /admin.teams.settings.setDescription`
- **Signature**: `def admin_teams_settings_set_description(token: str, content_type: ContentTypeOrStr, team_id: str, description: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `team_id`, `description`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `team_id` — form field · `description` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin.admin_teams_settings_set_discoverability

- **Route**: `POST /admin.teams.settings.setDiscoverability`
- **Signature**: `def admin_teams_settings_set_discoverability(token: str, content_type: ContentTypeOrStr, team_id: str, discoverability: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `team_id`, `discoverability`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `team_id` — form field · `discoverability` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin.admin_teams_settings_set_icon

- **Route**: `POST /admin.teams.settings.setIcon`
- **Signature**: `def admin_teams_settings_set_icon(content_type: ContentTypeOrStr, token: str, image_url: str, team_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`, `token`, `image_url`, `team_id`
- **Params**: `content_type` — header `Content-Type` · `token` — form field · `image_url` — form field · `team_id` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin.admin_teams_settings_set_name

- **Route**: `POST /admin.teams.settings.setName`
- **Signature**: `def admin_teams_settings_set_name(token: str, content_type: ContentTypeOrStr, team_id: str, name: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `team_id`, `name`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `team_id` — form field · `name` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin.admin_usergroups_add_channels

- **Route**: `POST /admin.usergroups.addChannels`
- **Signature**: `def admin_usergroups_add_channels(token: str, content_type: ContentTypeOrStr, usergroup_id: str, channel_ids: str, *, team_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `usergroup_id`, `channel_ids`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `usergroup_id` — form field · `channel_ids` — form field · `team_id` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin.admin_usergroups_add_teams

- **Route**: `POST /admin.usergroups.addTeams`
- **Signature**: `def admin_usergroups_add_teams(token: str, content_type: ContentTypeOrStr, usergroup_id: str, team_ids: str, *, auto_provision: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `usergroup_id`, `team_ids`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `usergroup_id` — form field · `team_ids` — form field · `auto_provision` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin.admin_usergroups_list_channels

- **Route**: `GET /admin.usergroups.listChannels`
- **Signature**: `def admin_usergroups_list_channels(usergroup_id: str, token: str, content_type: ContentTypeOrStr, *, team_id: str | None = None, include_num_members: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `usergroup_id`, `token`, `content_type`
- **Params**: `usergroup_id` — query · `team_id` — query · `include_num_members` — query · `token` — header · `content_type` — header `Content-Type`
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin.admin_usergroups_remove_channels

- **Route**: `POST /admin.usergroups.removeChannels`
- **Signature**: `def admin_usergroups_remove_channels(token: str, content_type: ContentTypeOrStr, usergroup_id: str, channel_ids: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `usergroup_id`, `channel_ids`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `usergroup_id` — form field · `channel_ids` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin.admin_users_assign

- **Route**: `POST /admin.users.assign`
- **Signature**: `def admin_users_assign(token: str, content_type: ContentTypeOrStr, team_id: str, user_id: str, *, is_restricted: bool | None = None, is_ultra_restricted: bool | None = None, channel_ids: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `team_id`, `user_id`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `team_id` — form field · `user_id` — form field · `is_restricted` — form field · `is_ultra_restricted` — form field · `channel_ids` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin.admin_users_invite

- **Route**: `POST /admin.users.invite`
- **Signature**: `def admin_users_invite(token: str, content_type: ContentTypeOrStr, team_id: str, email: str, channel_ids: str, *, custom_message: str | None = None, real_name: str | None = None, resend: bool | None = None, is_restricted: bool | None = None, is_ultra_restricted: bool | None = None, guest_expiration_ts: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `team_id`, `email`, `channel_ids`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `team_id` — form field · `email` — form field · `channel_ids` — form field · `custom_message` — form field · `real_name` — form field · `resend` — form field · `is_restricted` — form field · `is_ultra_restricted` — form field · `guest_expiration_ts` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin.admin_users_list

- **Route**: `GET /admin.users.list`
- **Signature**: `def admin_users_list(team_id: str, token: str, content_type: ContentTypeOrStr, *, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `team_id`, `token`, `content_type`
- **Params**: `team_id` — query · `cursor` — query · `limit` — query · `token` — header · `content_type` — header `Content-Type`
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin.admin_users_remove

- **Route**: `POST /admin.users.remove`
- **Signature**: `def admin_users_remove(token: str, content_type: ContentTypeOrStr, team_id: str, user_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `team_id`, `user_id`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `team_id` — form field · `user_id` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin.admin_users_session_invalidate

- **Route**: `POST /admin.users.session.invalidate`
- **Signature**: `def admin_users_session_invalidate(token: str, content_type: ContentTypeOrStr, team_id: str, session_id: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `team_id`, `session_id`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `team_id` — form field · `session_id` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin.admin_users_session_reset

- **Route**: `POST /admin.users.session.reset`
- **Signature**: `def admin_users_session_reset(token: str, content_type: ContentTypeOrStr, user_id: str, *, mobile_only: bool | None = None, web_only: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `user_id`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `user_id` — form field · `mobile_only` — form field · `web_only` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin.admin_users_set_admin

- **Route**: `POST /admin.users.setAdmin`
- **Signature**: `def admin_users_set_admin(token: str, content_type: ContentTypeOrStr, team_id: str, user_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `team_id`, `user_id`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `team_id` — form field · `user_id` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin.admin_users_set_expiration

- **Route**: `POST /admin.users.setExpiration`
- **Signature**: `def admin_users_set_expiration(token: str, content_type: ContentTypeOrStr, team_id: str, user_id: str, expiration_ts: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `team_id`, `user_id`, `expiration_ts`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `team_id` — form field · `user_id` — form field · `expiration_ts` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin.admin_users_set_owner

- **Route**: `POST /admin.users.setOwner`
- **Signature**: `def admin_users_set_owner(token: str, content_type: ContentTypeOrStr, team_id: str, user_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `team_id`, `user_id`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `team_id` — form field · `user_id` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin.admin_users_set_regular

- **Route**: `POST /admin.users.setRegular`
- **Signature**: `def admin_users_set_regular(token: str, content_type: ContentTypeOrStr, team_id: str, user_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `team_id`, `user_id`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `team_id` — form field · `user_id` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

