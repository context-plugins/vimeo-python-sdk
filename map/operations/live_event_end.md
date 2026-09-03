<!-- Generated file — do not edit; regenerated with the SDK. -->

# LiveEventEnd — operations

Accessor: `client.live_event_end` · Source: `vimeo_api/apis/live_event_end.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.live_event_end.end_live_event

- **Route**: `POST /users/{user_id}/live_events/{live_event_id}/end`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def end_live_event(live_event_id: float, user_id: str, *, clip_id: float | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`, `user_id`
- **Params**: `live_event_id` — path · `user_id` — path · `clip_id` — query
- **Returns (parsed)**: `Video`
- **Returns (raw)**: `ApiResult[Video, EndLiveEventErrorBody]`
- **Error**: `EndLiveEventErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 403, 404, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Video` | `vimeo_api/models/video.py` |
| `EndLiveEventErrorBody` | `vimeo_api/errors/end_live_event_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.live_event_end.end_live_event_alt1

- **Route**: `POST /live_events/{live_event_id}/end`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def end_live_event_alt1(live_event_id: float, *, clip_id: float | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`
- **Params**: `live_event_id` — path · `clip_id` — query
- **Returns (parsed)**: `Video`
- **Returns (raw)**: `ApiResult[Video, EndLiveEventAlt1ErrorBody]`
- **Error**: `EndLiveEventAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 403, 404, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Video` | `vimeo_api/models/video.py` |
| `EndLiveEventAlt1ErrorBody` | `vimeo_api/errors/end_live_event_alt1_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.live_event_end.end_live_event_alt2

- **Route**: `POST /me/live_events/{live_event_id}/end`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def end_live_event_alt2(live_event_id: float, *, clip_id: float | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`
- **Params**: `live_event_id` — path · `clip_id` — query
- **Returns (parsed)**: `Video`
- **Returns (raw)**: `ApiResult[Video, EndLiveEventAlt2ErrorBody]`
- **Error**: `EndLiveEventAlt2ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 403, 404, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Video` | `vimeo_api/models/video.py` |
| `EndLiveEventAlt2ErrorBody` | `vimeo_api/errors/end_live_event_alt2_error.py` |
| `Error` | `vimeo_api/models/error.py` |

