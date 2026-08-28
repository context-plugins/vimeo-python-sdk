<!-- Generated file — do not edit; regenerated with the SDK. -->

# VideosLanguages — operations

Accessor: `client.videos_languages` · Source: `vimeo/apis/videos_languages.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.videos_languages.get_languages

- **Route**: `GET /languages`
- **Signature**: `def get_languages(*, filter: Filter7OrStr | None = None, page: float | None = None, per_page: float | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `filter` — query · `page` — query · `per_page` — query
- **Returns (parsed)**: `LanguageConnection`
- **Returns (raw)**: `ApiResult[LanguageConnection, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Filter7OrStr` | `vimeo/models/enums/filter7.py` |
| `LanguageConnection` | `vimeo/models/language_connection.py` |

