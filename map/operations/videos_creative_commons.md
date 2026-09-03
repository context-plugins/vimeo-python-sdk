<!-- Generated file — do not edit; regenerated with the SDK. -->

# VideosCreativeCommons — operations

Accessor: `client.videos_creative_commons` · Source: `vimeo_api/apis/videos_creative_commons.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.videos_creative_commons.get_cc_licenses

- **Route**: `GET /creativecommons`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_cc_licenses(*, page: float | None = None, per_page: float | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page` — query · `per_page` — query
- **Returns (parsed)**: `CreativeCommonsConnection`
- **Returns (raw)**: `ApiResult[CreativeCommonsConnection, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreativeCommonsConnection` | `vimeo_api/models/creative_commons_connection.py` |

