<!-- Generated file — do not edit; regenerated with the SDK. -->

# AuthApi — operations

Accessor: `client.auth_api` · Source: `slack_web_api/apis/auth_api.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.auth_api.auth_revoke

- **Route**: `GET /auth.revoke`
- **Signature**: `def auth_revoke(token: str, content_type: ContentTypeOrStr, *, test: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`
- **Params**: `token` — query · `test` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `AuthRevokeschema`
- **Returns (raw)**: `ApiResult[AuthRevokeschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `AuthRevokeschema` | `slack_web_api/models/auth_revokeschema.py` |

### client.auth_api.auth_test

- **Route**: `GET /auth.test`
- **Signature**: `def auth_test(token: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`
- **Params**: `token` — header · `content_type` — header `Content-Type`
- **Returns (parsed)**: `AuthTestsuccessschema`
- **Returns (raw)**: `ApiResult[AuthTestsuccessschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `AuthTestsuccessschema` | `slack_web_api/models/auth_testsuccessschema.py` |

