<!-- Generated file — do not edit; regenerated with the SDK. -->

# Calls — operations

Accessor: `client.calls` · Source: `slack_web_api/apis/calls.py` · 6 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.calls.calls_add

- **Route**: `POST /calls.add`
- **Signature**: `def calls_add(token: str, content_type: ContentTypeOrStr, external_unique_id: str, join_url: str, *, external_display_id: str | None = None, desktop_app_join_url: str | None = None, date_start: int | None = None, title: str | None = None, created_by: str | None = None, users: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `external_unique_id`, `join_url`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `external_unique_id` — form field · `join_url` — form field · `external_display_id` — form field · `desktop_app_join_url` — form field · `date_start` — form field · `title` — form field · `created_by` — form field · `users` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.calls.calls_end

- **Route**: `POST /calls.end`
- **Signature**: `def calls_end(token: str, content_type: ContentTypeOrStr, id: str, *, duration: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `id`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `id` — form field · `duration` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.calls.calls_info

- **Route**: `GET /calls.info`
- **Signature**: `def calls_info(id: str, token: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`, `token`, `content_type`
- **Params**: `id` — query · `token` — header · `content_type` — header `Content-Type`
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.calls.calls_participants_add

- **Route**: `POST /calls.participants.add`
- **Signature**: `def calls_participants_add(token: str, content_type: ContentTypeOrStr, id: str, users: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `id`, `users`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `id` — form field · `users` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.calls.calls_participants_remove

- **Route**: `POST /calls.participants.remove`
- **Signature**: `def calls_participants_remove(token: str, content_type: ContentTypeOrStr, id: str, users: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `id`, `users`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `id` — form field · `users` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.calls.calls_update

- **Route**: `POST /calls.update`
- **Signature**: `def calls_update(token: str, content_type: ContentTypeOrStr, id: str, *, title: str | None = None, join_url: str | None = None, desktop_app_join_url: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `id`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `id` — form field · `title` — form field · `join_url` — form field · `desktop_app_join_url` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

