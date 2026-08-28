<!-- Generated file — do not edit; regenerated with the SDK. -->

# TeamApi — operations

Accessor: `client.team_api` · Source: `slack_web_api/apis/team_api.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.team_api.team_access_logs

- **Route**: `GET /team.accessLogs`
- **Signature**: `def team_access_logs(token: str, content_type: ContentTypeOrStr, *, before: str | None = None, count: str | None = None, page: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`
- **Params**: `token` — query · `before` — query · `count` — query · `page` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `TeamAccessLogsschema`
- **Returns (raw)**: `ApiResult[TeamAccessLogsschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `TeamAccessLogsschema` | `slack_web_api/models/team_access_logsschema.py` |

### client.team_api.team_billable_info

- **Route**: `GET /team.billableInfo`
- **Signature**: `def team_billable_info(token: str, content_type: ContentTypeOrStr, *, user: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`
- **Params**: `token` — query · `user` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.team_api.team_info

- **Route**: `GET /team.info`
- **Signature**: `def team_info(token: str, content_type: ContentTypeOrStr, *, team: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`
- **Params**: `token` — query · `team` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `TeamInfoschema`
- **Returns (raw)**: `ApiResult[TeamInfoschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `TeamInfoschema` | `slack_web_api/models/team_infoschema.py` |

### client.team_api.team_integration_logs

- **Route**: `GET /team.integrationLogs`
- **Signature**: `def team_integration_logs(token: str, content_type: ContentTypeOrStr, *, app_id: str | None = None, change_type: str | None = None, count: str | None = None, page: str | None = None, service_id: str | None = None, user: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`
- **Params**: `token` — query · `app_id` — query · `change_type` — query · `count` — query · `page` — query · `service_id` — query · `user` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `TeamIntegrationLogsschema`
- **Returns (raw)**: `ApiResult[TeamIntegrationLogsschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `TeamIntegrationLogsschema` | `slack_web_api/models/team_integration_logsschema.py` |

### client.team_api.team_profile_get

- **Route**: `GET /team.profile.get`
- **Signature**: `def team_profile_get(token: str, content_type: ContentTypeOrStr, *, visibility: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`
- **Params**: `token` — query · `visibility` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `TeamProfileGetsuccessschema`
- **Returns (raw)**: `ApiResult[TeamProfileGetsuccessschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `TeamProfileGetsuccessschema` | `slack_web_api/models/team_profile_getsuccessschema.py` |

