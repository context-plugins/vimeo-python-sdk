<!-- Generated file — do not edit; regenerated with the SDK. -->

# TagsEssentials — operations

Accessor: `client.tags_essentials` · Source: `vimeo/apis/tags_essentials.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.tags_essentials.get_tag

- **Route**: `GET /tags/{word}`
- **Signature**: `def get_tag(word: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `word`
- **Params**: `word` — path
- **Returns (parsed)**: `Tag`
- **Returns (raw)**: `ApiResult[Tag, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Tag` | `vimeo/models/tag.py` |

