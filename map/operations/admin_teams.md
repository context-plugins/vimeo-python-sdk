<!-- Generated file — do not edit; regenerated with the SDK. -->

# AdminTeams — operations

Accessor: `client.admin_teams` · Source: `slack_web_api/apis/admin_teams.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.admin_teams.admin_teams_create

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

### client.admin_teams.admin_teams_list

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

