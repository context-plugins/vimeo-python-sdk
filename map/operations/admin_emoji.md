<!-- Generated file — do not edit; regenerated with the SDK. -->

# AdminEmoji — operations

Accessor: `client.admin_emoji` · Source: `slack_web_api/apis/admin_emoji.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.admin_emoji.admin_emoji_add

- **Route**: `POST /admin.emoji.add`
- **Signature**: `def admin_emoji_add(content_type: ContentTypeOrStr, token: str, name: str, url: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`, `token`, `name`, `url`
- **Params**: `content_type` — header `Content-Type` · `token` — form field · `name` — form field · `url` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin_emoji.admin_emoji_add_alias

- **Route**: `POST /admin.emoji.addAlias`
- **Signature**: `def admin_emoji_add_alias(content_type: ContentTypeOrStr, token: str, name: str, alias_for: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`, `token`, `name`, `alias_for`
- **Params**: `content_type` — header `Content-Type` · `token` — form field · `name` — form field · `alias_for` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin_emoji.admin_emoji_list

- **Route**: `GET /admin.emoji.list`
- **Signature**: `def admin_emoji_list(token: str, content_type: ContentTypeOrStr, *, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`
- **Params**: `token` — query · `cursor` — query · `limit` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin_emoji.admin_emoji_remove

- **Route**: `POST /admin.emoji.remove`
- **Signature**: `def admin_emoji_remove(content_type: ContentTypeOrStr, token: str, name: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`, `token`, `name`
- **Params**: `content_type` — header `Content-Type` · `token` — form field · `name` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.admin_emoji.admin_emoji_rename

- **Route**: `POST /admin.emoji.rename`
- **Signature**: `def admin_emoji_rename(content_type: ContentTypeOrStr, token: str, name: str, new_name: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`, `token`, `name`, `new_name`
- **Params**: `content_type` — header `Content-Type` · `token` — form field · `name` — form field · `new_name` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

