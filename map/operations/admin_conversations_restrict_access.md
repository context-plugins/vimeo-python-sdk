<!-- Generated file — do not edit; regenerated with the SDK. -->

# AdminConversationsRestrictAccess — operations

Accessor: `client.admin_conversations_restrict_access` · Source: `slack_web_api/apis/admin_conversations_restrict_access.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.admin_conversations_restrict_access.admin_conversations_restrict_access_add_group

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

### client.admin_conversations_restrict_access.admin_conversations_restrict_access_list_groups

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

### client.admin_conversations_restrict_access.admin_conversations_restrict_access_remove_group

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

