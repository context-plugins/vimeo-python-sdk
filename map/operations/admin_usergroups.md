<!-- Generated file — do not edit; regenerated with the SDK. -->

# AdminUsergroups — operations

Accessor: `client.admin_usergroups` · Source: `slack_web_api/apis/admin_usergroups.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.admin_usergroups.admin_usergroups_add_channels

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

### client.admin_usergroups.admin_usergroups_add_teams

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

### client.admin_usergroups.admin_usergroups_list_channels

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

### client.admin_usergroups.admin_usergroups_remove_channels

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

