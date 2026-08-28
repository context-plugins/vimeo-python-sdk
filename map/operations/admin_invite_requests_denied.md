<!-- Generated file — do not edit; regenerated with the SDK. -->

# AdminInviteRequestsDenied — operations

Accessor: `client.admin_invite_requests_denied` · Source: `slack_web_api/apis/admin_invite_requests_denied.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.admin_invite_requests_denied.admin_invite_requests_denied_list

- **Route**: `GET /admin.inviteRequests.denied.list`
- **Signature**: `def admin_invite_requests_denied_list(token: str, content_type: ContentTypeOrStr, *, team_id: str | None = None, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`
- **Params**: `team_id` — query · `cursor` — query · `limit` — query · `token` — header · `content_type` — header `Content-Type`
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

