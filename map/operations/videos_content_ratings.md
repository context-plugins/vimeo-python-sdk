<!-- Generated file — do not edit; regenerated with the SDK. -->

# VideosContentRatings — operations

Accessor: `client.videos_content_ratings` · Source: `vimeo_api/apis/videos_content_ratings.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.videos_content_ratings.get_content_ratings

- **Route**: `GET /contentratings`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_content_ratings(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `ContentRatingConnection`
- **Returns (raw)**: `ApiResult[ContentRatingConnection, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentRatingConnection` | `vimeo_api/models/content_rating_connection.py` |

