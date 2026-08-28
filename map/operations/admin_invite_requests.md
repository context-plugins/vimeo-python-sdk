<!-- Generated file — do not edit; regenerated with the SDK. -->

# AdminInviteRequests — operations

Accessor: `client.admin_invite_requests` · Source: `slack_web_api/apis/admin_invite_requests.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.admin_invite_requests.admin_invite_requests_approve

- **Route**: `POST /admin.inviteRequests.approve`
- **Signature**: `def admin_invite_requests_approve(token: str, content_type: ContentTypeOrStr, invite_request_id: str, *, team_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `invite_request_id`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `invite_request_id` — form field · `team_id` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin_invite_requests.admin_invite_requests_deny

- **Route**: `POST /admin.inviteRequests.deny`
- **Signature**: `def admin_invite_requests_deny(token: str, content_type: ContentTypeOrStr, invite_request_id: str, *, team_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `invite_request_id`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `invite_request_id` — form field · `team_id` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin_invite_requests.admin_invite_requests_list

- **Route**: `GET /admin.inviteRequests.list`
- **Signature**: `def admin_invite_requests_list(token: str, content_type: ContentTypeOrStr, *, team_id: str | None = None, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`
- **Params**: `team_id` — query · `cursor` — query · `limit` — query · `token` — header · `content_type` — header `Content-Type`
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

