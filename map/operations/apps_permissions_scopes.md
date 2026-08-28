<!-- Generated file — do not edit; regenerated with the SDK. -->

# AppsPermissionsScopes — operations

Accessor: `client.apps_permissions_scopes` · Source: `slack_web_api/apis/apps_permissions_scopes.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.apps_permissions_scopes.apps_permissions_scopes_list

- **Route**: `GET /apps.permissions.scopes.list`
- **Signature**: `def apps_permissions_scopes_list(token: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`
- **Params**: `token` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `ApiPermissionsScopesListsuccessschema`
- **Returns (raw)**: `ApiResult[ApiPermissionsScopesListsuccessschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `ApiPermissionsScopesListsuccessschema` | `slack_web_api/models/api_permissions_scopes_listsuccessschema.py` |

