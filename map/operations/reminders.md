<!-- Generated file — do not edit; regenerated with the SDK. -->

# Reminders — operations

Accessor: `client.reminders` · Source: `slack_web_api/apis/reminders.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.reminders.reminders_add

- **Route**: `POST /reminders.add`
- **Signature**: `def reminders_add(token: str, content_type: ContentTypeOrStr, text: str, time: str, *, user: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `text`, `time`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `text` — form field · `time` — form field · `user` — form field
- **Returns (parsed)**: `RemindersAddschema`
- **Returns (raw)**: `ApiResult[RemindersAddschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `RemindersAddschema` | `slack_web_api/models/reminders_addschema.py` |

### client.reminders.reminders_complete

- **Route**: `POST /reminders.complete`
- **Signature**: `def reminders_complete(content_type: ContentTypeOrStr, *, token: str | None = None, reminder: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`
- **Params**: `content_type` — header `Content-Type` · `token` — header · `reminder` — form field
- **Returns (parsed)**: `RemindersCompleteschema`
- **Returns (raw)**: `ApiResult[RemindersCompleteschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `RemindersCompleteschema` | `slack_web_api/models/reminders_completeschema.py` |

### client.reminders.reminders_delete

- **Route**: `POST /reminders.delete`
- **Signature**: `def reminders_delete(content_type: ContentTypeOrStr, *, token: str | None = None, reminder: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`
- **Params**: `content_type` — header `Content-Type` · `token` — header · `reminder` — form field
- **Returns (parsed)**: `RemindersDeleteschema`
- **Returns (raw)**: `ApiResult[RemindersDeleteschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `RemindersDeleteschema` | `slack_web_api/models/reminders_deleteschema.py` |

### client.reminders.reminders_info

- **Route**: `GET /reminders.info`
- **Signature**: `def reminders_info(content_type: ContentTypeOrStr, *, token: str | None = None, reminder: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`
- **Params**: `token` — query · `reminder` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `RemindersInfoschema`
- **Returns (raw)**: `ApiResult[RemindersInfoschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `RemindersInfoschema` | `slack_web_api/models/reminders_infoschema.py` |

### client.reminders.reminders_list

- **Route**: `GET /reminders.list`
- **Signature**: `def reminders_list(content_type: ContentTypeOrStr, *, token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`
- **Params**: `token` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `RemindersListschema`
- **Returns (raw)**: `ApiResult[RemindersListschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `RemindersListschema` | `slack_web_api/models/reminders_listschema.py` |

