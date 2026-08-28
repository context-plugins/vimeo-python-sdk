<!-- Generated file — do not edit; regenerated with the SDK. -->

# AdminUsersSession — operations

Accessor: `client.admin_users_session` · Source: `slack_web_api/apis/admin_users_session.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.admin_users_session.admin_users_session_invalidate

- **Route**: `POST /admin.users.session.invalidate`
- **Signature**: `def admin_users_session_invalidate(token: str, content_type: ContentTypeOrStr, team_id: str, session_id: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `team_id`, `session_id`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `team_id` — form field · `session_id` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin_users_session.admin_users_session_reset

- **Route**: `POST /admin.users.session.reset`
- **Signature**: `def admin_users_session_reset(token: str, content_type: ContentTypeOrStr, user_id: str, *, mobile_only: bool | None = None, web_only: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `user_id`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `user_id` — form field · `mobile_only` — form field · `web_only` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

