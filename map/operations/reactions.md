<!-- Generated file — do not edit; regenerated with the SDK. -->

# Reactions — operations

Accessor: `client.reactions` · Source: `slack_web_api/apis/reactions.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.reactions.reactions_add

- **Route**: `POST /reactions.add`
- **Signature**: `def reactions_add(token: str, content_type: ContentTypeOrStr, channel: str, name: str, timestamp: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `channel`, `name`, `timestamp`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `channel` — form field · `name` — form field · `timestamp` — form field
- **Returns (parsed)**: `ReactionsAddschema`
- **Returns (raw)**: `ApiResult[ReactionsAddschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `ReactionsAddschema` | `slack_web_api/models/reactions_addschema.py` |

### client.reactions.reactions_get

- **Route**: `GET /reactions.get`
- **Signature**: `def reactions_get(token: str, content_type: ContentTypeOrStr, *, channel: str | None = None, file: str | None = None, file_comment: str | None = None, full: bool | None = None, timestamp: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`
- **Params**: `token` — query · `channel` — query · `file` — query · `file_comment` — query · `full` — query · `timestamp` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |

### client.reactions.reactions_list

- **Route**: `GET /reactions.list`
- **Signature**: `def reactions_list(token: str, content_type: ContentTypeOrStr, *, user: str | None = None, full: bool | None = None, count: int | None = None, page: int | None = None, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`
- **Params**: `token` — query · `user` — query · `full` — query · `count` — query · `page` — query · `cursor` — query · `limit` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `ReactionsListschema`
- **Returns (raw)**: `ApiResult[ReactionsListschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `ReactionsListschema` | `slack_web_api/models/reactions_listschema.py` |

### client.reactions.reactions_remove

- **Route**: `POST /reactions.remove`
- **Signature**: `def reactions_remove(token: str, content_type: ContentTypeOrStr, name: str, *, file: str | None = None, file_comment: str | None = None, channel: str | None = None, timestamp: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `name`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `name` — form field · `file` — form field · `file_comment` — form field · `channel` — form field · `timestamp` — form field
- **Returns (parsed)**: `ReactionsRemoveschema`
- **Returns (raw)**: `ApiResult[ReactionsRemoveschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `ReactionsRemoveschema` | `slack_web_api/models/reactions_removeschema.py` |

