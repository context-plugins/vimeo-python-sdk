<!-- Generated file — do not edit; regenerated with the SDK. -->

# UsersProfile — operations

Accessor: `client.users_profile` · Source: `slack_web_api/apis/users_profile.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.users_profile.users_profile_get

- **Route**: `GET /users.profile.get`
- **Signature**: `def users_profile_get(token: str, content_type: ContentTypeOrStr, *, include_labels: bool | None = None, user: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`
- **Params**: `token` — query · `include_labels` — query · `user` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `UsersProfileGetschema`
- **Returns (raw)**: `ApiResult[UsersProfileGetschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `UsersProfileGetschema` | `slack_web_api/models/users_profile_getschema.py` |

### client.users_profile.users_profile_set

- **Route**: `POST /users.profile.set`
- **Signature**: `def users_profile_set(token: str, content_type: ContentTypeOrStr, *, name: str | None = None, profile: str | None = None, user: str | None = None, value: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `name` — form field · `profile` — form field · `user` — form field · `value` — form field
- **Returns (parsed)**: `UsersProfileSetschema`
- **Returns (raw)**: `ApiResult[UsersProfileSetschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `UsersProfileSetschema` | `slack_web_api/models/users_profile_setschema.py` |

