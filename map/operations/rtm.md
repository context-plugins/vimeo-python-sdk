<!-- Generated file — do not edit; regenerated with the SDK. -->

# Rtm — operations

Accessor: `client.rtm` · Source: `slack_web_api/apis/rtm.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.rtm.rtm_connect

- **Route**: `GET /rtm.connect`
- **Signature**: `def rtm_connect(token: str, content_type: ContentTypeOrStr, *, batch_presence_aware: bool | None = None, presence_sub: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`
- **Params**: `token` — query · `batch_presence_aware` — query · `presence_sub` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `RtmConnectschema`
- **Returns (raw)**: `ApiResult[RtmConnectschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `RtmConnectschema` | `slack_web_api/models/rtm_connectschema.py` |

