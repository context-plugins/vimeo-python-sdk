<!-- Generated file — do not edit; regenerated with the SDK. -->

# AdminAppsRestricted — operations

Accessor: `client.admin_apps_restricted` · Source: `slack_web_api/apis/admin_apps_restricted.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.admin_apps_restricted.admin_apps_restricted_list

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

