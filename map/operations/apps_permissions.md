<!-- Generated file — do not edit; regenerated with the SDK. -->

# AppsPermissions — operations

Accessor: `client.apps_permissions` · Source: `slack_web_api/apis/apps_permissions.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.apps_permissions.apps_permissions_info

- **Route**: `GET /apps.permissions.info`
- **Signature**: `def apps_permissions_info(content_type: ContentTypeOrStr, *, token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`
- **Params**: `token` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `AppsPermissionsInfoschema`
- **Returns (raw)**: `ApiResult[AppsPermissionsInfoschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `AppsPermissionsInfoschema` | `slack_web_api/models/apps_permissions_infoschema.py` |

### client.apps_permissions.apps_permissions_request

- **Route**: `GET /apps.permissions.request`
- **Signature**: `def apps_permissions_request(token: str, scopes: str, trigger_id: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `scopes`, `trigger_id`, `content_type`
- **Params**: `token` — query · `scopes` — query · `trigger_id` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `AppsPermissionsRequestschema`
- **Returns (raw)**: `ApiResult[AppsPermissionsRequestschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `AppsPermissionsRequestschema` | `slack_web_api/models/apps_permissions_requestschema.py` |

