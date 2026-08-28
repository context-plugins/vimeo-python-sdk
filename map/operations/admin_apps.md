<!-- Generated file — do not edit; regenerated with the SDK. -->

# AdminApps — operations

Accessor: `client.admin_apps` · Source: `slack_web_api/apis/admin_apps.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.admin_apps.admin_apps_approve

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

### client.admin_apps.admin_apps_restrict

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

