<!-- Generated file — do not edit; regenerated with the SDK. -->

# Apps — operations

Accessor: `client.apps` · Source: `slack_web_api/apis/apps.py` · 8 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.apps.apps_event_authorizations_list

- **Route**: `GET /apps.event.authorizations.list`
- **Signature**: `def apps_event_authorizations_list(event_context: str, token: str, content_type: ContentTypeOrStr, *, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `event_context`, `token`, `content_type`
- **Params**: `event_context` — query · `cursor` — query · `limit` — query · `token` — header · `content_type` — header `Content-Type`
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.apps.apps_permissions_info

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

### client.apps.apps_permissions_request

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

### client.apps.apps_permissions_resources_list

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

### client.apps.apps_permissions_scopes_list

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

### client.apps.apps_permissions_users_list

- **Route**: `GET /apps.permissions.users.list`
- **Signature**: `def apps_permissions_users_list(token: str, content_type: ContentTypeOrStr, *, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`
- **Params**: `token` — query · `cursor` — query · `limit` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.apps.apps_permissions_users_request

- **Route**: `GET /apps.permissions.users.request`
- **Signature**: `def apps_permissions_users_request(token: str, scopes: str, trigger_id: str, user: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `scopes`, `trigger_id`, `user`, `content_type`
- **Params**: `token` — query · `scopes` — query · `trigger_id` — query · `user` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.apps.apps_uninstall

- **Route**: `GET /apps.uninstall`
- **Signature**: `def apps_uninstall(content_type: ContentTypeOrStr, *, token: str | None = None, client_id: str | None = None, client_secret: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`
- **Params**: `token` — query · `client_id` — query · `client_secret` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `AppsUninstallschema`
- **Returns (raw)**: `ApiResult[AppsUninstallschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `AppsUninstallschema` | `slack_web_api/models/apps_uninstallschema.py` |

