<!-- Generated file — do not edit; regenerated with the SDK. -->

# AdminTeamsSettings — operations

Accessor: `client.admin_teams_settings` · Source: `slack_web_api/apis/admin_teams_settings.py` · 6 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.admin_teams_settings.admin_teams_settings_info

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

### client.admin_teams_settings.admin_teams_settings_set_default_channels

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

### client.admin_teams_settings.admin_teams_settings_set_description

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

### client.admin_teams_settings.admin_teams_settings_set_discoverability

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

### client.admin_teams_settings.admin_teams_settings_set_icon

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

### client.admin_teams_settings.admin_teams_settings_set_name

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

