<!-- Generated file — do not edit; regenerated with the SDK. -->

# Bots — operations

Accessor: `client.bots` · Source: `slack_web_api/apis/bots.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.bots.bots_info

- **Route**: `GET /bots.info`
- **Signature**: `def bots_info(token: str, content_type: ContentTypeOrStr, *, bot: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`
- **Params**: `token` — query · `bot` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `BotsInfoschema`
- **Returns (raw)**: `ApiResult[BotsInfoschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `BotsInfoschema` | `slack_web_api/models/bots_infoschema.py` |

