<!-- Generated file — do not edit; regenerated with the SDK. -->

# Search — operations

Accessor: `client.search` · Source: `slack_web_api/apis/search.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.search.search_messages

- **Route**: `GET /search.messages`
- **Signature**: `def search_messages(token: str, query: str, content_type: ContentTypeOrStr, *, count: int | None = None, highlight: bool | None = None, page: int | None = None, sort: str | None = None, sort_dir: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `query`, `content_type`
- **Params**: `token` — query · `query` — query · `count` — query · `highlight` — query · `page` — query · `sort` — query · `sort_dir` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

