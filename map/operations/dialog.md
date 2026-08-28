<!-- Generated file — do not edit; regenerated with the SDK. -->

# Dialog — operations

Accessor: `client.dialog` · Source: `slack_web_api/apis/dialog.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.dialog.dialog_open

- **Route**: `GET /dialog.open`
- **Signature**: `def dialog_open(dialog: str, trigger_id: str, token: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `dialog`, `trigger_id`, `token`, `content_type`
- **Params**: `dialog` — query · `trigger_id` — query · `token` — header · `content_type` — header `Content-Type`
- **Returns (parsed)**: `DialogOpenschema`
- **Returns (raw)**: `ApiResult[DialogOpenschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `DialogOpenschema` | `slack_web_api/models/dialog_openschema.py` |

