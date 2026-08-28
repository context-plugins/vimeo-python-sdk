<!-- Generated file — do not edit; regenerated with the SDK. -->

# AppsPermissionsResources — operations

Accessor: `client.apps_permissions_resources` · Source: `slack_web_api/apis/apps_permissions_resources.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.apps_permissions_resources.apps_permissions_resources_list

- **Route**: `GET /apps.permissions.resources.list`
- **Signature**: `def apps_permissions_resources_list(token: str, content_type: ContentTypeOrStr, *, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`
- **Params**: `token` — query · `cursor` — query · `limit` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `AppsPermissionsResourcesListsuccessschema`
- **Returns (raw)**: `ApiResult[AppsPermissionsResourcesListsuccessschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `AppsPermissionsResourcesListsuccessschema` | `slack_web_api/models/apps_permissions_resources_listsuccessschema.py` |

