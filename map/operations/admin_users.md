<!-- Generated file — do not edit; regenerated with the SDK. -->

# AdminUsers — operations

Accessor: `client.admin_users` · Source: `slack_web_api/apis/admin_users.py` · 8 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.admin_users.admin_users_assign

- **Route**: `POST /admin.users.assign`
- **Signature**: `def admin_users_assign(token: str, content_type: ContentTypeOrStr, team_id: str, user_id: str, *, is_restricted: bool | None = None, is_ultra_restricted: bool | None = None, channel_ids: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `team_id`, `user_id`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `team_id` — form field · `user_id` — form field · `is_restricted` — form field · `is_ultra_restricted` — form field · `channel_ids` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin_users.admin_users_invite

- **Route**: `POST /admin.users.invite`
- **Signature**: `def admin_users_invite(token: str, content_type: ContentTypeOrStr, team_id: str, email: str, channel_ids: str, *, custom_message: str | None = None, real_name: str | None = None, resend: bool | None = None, is_restricted: bool | None = None, is_ultra_restricted: bool | None = None, guest_expiration_ts: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `team_id`, `email`, `channel_ids`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `team_id` — form field · `email` — form field · `channel_ids` — form field · `custom_message` — form field · `real_name` — form field · `resend` — form field · `is_restricted` — form field · `is_ultra_restricted` — form field · `guest_expiration_ts` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin_users.admin_users_list

- **Route**: `GET /admin.users.list`
- **Signature**: `def admin_users_list(team_id: str, token: str, content_type: ContentTypeOrStr, *, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `team_id`, `token`, `content_type`
- **Params**: `team_id` — query · `cursor` — query · `limit` — query · `token` — header · `content_type` — header `Content-Type`
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin_users.admin_users_remove

- **Route**: `POST /admin.users.remove`
- **Signature**: `def admin_users_remove(token: str, content_type: ContentTypeOrStr, team_id: str, user_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `team_id`, `user_id`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `team_id` — form field · `user_id` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin_users.admin_users_set_admin

- **Route**: `POST /admin.users.setAdmin`
- **Signature**: `def admin_users_set_admin(token: str, content_type: ContentTypeOrStr, team_id: str, user_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `team_id`, `user_id`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `team_id` — form field · `user_id` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin_users.admin_users_set_expiration

- **Route**: `POST /admin.users.setExpiration`
- **Signature**: `def admin_users_set_expiration(token: str, content_type: ContentTypeOrStr, team_id: str, user_id: str, expiration_ts: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `team_id`, `user_id`, `expiration_ts`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `team_id` — form field · `user_id` — form field · `expiration_ts` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin_users.admin_users_set_owner

- **Route**: `POST /admin.users.setOwner`
- **Signature**: `def admin_users_set_owner(token: str, content_type: ContentTypeOrStr, team_id: str, user_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `team_id`, `user_id`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `team_id` — form field · `user_id` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin_users.admin_users_set_regular

- **Route**: `POST /admin.users.setRegular`
- **Signature**: `def admin_users_set_regular(token: str, content_type: ContentTypeOrStr, team_id: str, user_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `team_id`, `user_id`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `team_id` — form field · `user_id` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

