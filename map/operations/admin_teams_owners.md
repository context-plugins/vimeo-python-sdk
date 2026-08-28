<!-- Generated file — do not edit; regenerated with the SDK. -->

# AdminTeamsOwners — operations

Accessor: `client.admin_teams_owners` · Source: `slack_web_api/apis/admin_teams_owners.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.admin_teams_owners.admin_teams_owners_list

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

