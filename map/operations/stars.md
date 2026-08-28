<!-- Generated file — do not edit; regenerated with the SDK. -->

# Stars — operations

Accessor: `client.stars` · Source: `slack_web_api/apis/stars.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.stars.stars_add

- **Route**: `POST /stars.add`
- **Signature**: `def stars_add(token: str, content_type: ContentTypeOrStr, *, channel: str | None = None, file: str | None = None, file_comment: str | None = None, timestamp: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `channel` — form field · `file` — form field · `file_comment` — form field · `timestamp` — form field
- **Returns (parsed)**: `StarsAddschema`
- **Returns (raw)**: `ApiResult[StarsAddschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `StarsAddschema` | `slack_web_api/models/stars_addschema.py` |

### client.stars.stars_list

- **Route**: `GET /stars.list`
- **Signature**: `def stars_list(content_type: ContentTypeOrStr, *, token: str | None = None, count: str | None = None, page: str | None = None, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`
- **Params**: `token` — query · `count` — query · `page` — query · `cursor` — query · `limit` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `StarsListschema`
- **Returns (raw)**: `ApiResult[StarsListschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `StarsListschema` | `slack_web_api/models/stars_listschema.py` |

### client.stars.stars_remove

- **Route**: `POST /stars.remove`
- **Signature**: `def stars_remove(token: str, content_type: ContentTypeOrStr, *, channel: str | None = None, file: str | None = None, file_comment: str | None = None, timestamp: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `channel` — form field · `file` — form field · `file_comment` — form field · `timestamp` — form field
- **Returns (parsed)**: `StarsRemoveschema`
- **Returns (raw)**: `ApiResult[StarsRemoveschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `StarsRemoveschema` | `slack_web_api/models/stars_removeschema.py` |

