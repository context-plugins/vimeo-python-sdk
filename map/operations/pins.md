<!-- Generated file — do not edit; regenerated with the SDK. -->

# Pins — operations

Accessor: `client.pins` · Source: `slack_web_api/apis/pins.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.pins.pins_add

- **Route**: `POST /pins.add`
- **Signature**: `def pins_add(token: str, content_type: ContentTypeOrStr, channel: str, *, timestamp: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `channel`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `channel` — form field · `timestamp` — form field
- **Returns (parsed)**: `PinsAddschema`
- **Returns (raw)**: `ApiResult[PinsAddschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `PinsAddschema` | `slack_web_api/models/pins_addschema.py` |

### client.pins.pins_list

- **Route**: `GET /pins.list`
- **Signature**: `def pins_list(token: str, channel: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `channel`, `content_type`
- **Params**: `token` — query · `channel` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |

### client.pins.pins_remove

- **Route**: `POST /pins.remove`
- **Signature**: `def pins_remove(token: str, content_type: ContentTypeOrStr, channel: str, *, timestamp: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `channel`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `channel` — form field · `timestamp` — form field
- **Returns (parsed)**: `PinsRemoveschema`
- **Returns (raw)**: `ApiResult[PinsRemoveschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `PinsRemoveschema` | `slack_web_api/models/pins_removeschema.py` |

