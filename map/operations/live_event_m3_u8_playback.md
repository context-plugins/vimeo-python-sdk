<!-- Generated file — do not edit; regenerated with the SDK. -->

# LiveEventM3U8Playback — operations

Accessor: `client.live_event_m3_u8_playback` · Source: `vimeo/apis/live_event_m3_u8_playback.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.live_event_m3_u8_playback.get_live_event_m3u8_playback

- **Route**: `GET /users/{user_id}/live_events/{live_event_id}/m3u8_playback`
- **Signature**: `def get_live_event_m3u8_playback(live_event_id: float, user_id: float, *, dvr: float | None = None, max_fps_fhd: float | None = None, ttl: float | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`, `user_id`
- **Params**: `live_event_id` — path · `user_id` — path · `dvr` — query · `max_fps_fhd` — query · `ttl` — query
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, GetLiveEventM3U8PlaybackErrorBody]`
- **Error**: `GetLiveEventM3U8PlaybackErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401, 403, 404, 500, 503] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetLiveEventM3U8PlaybackErrorBody` | `vimeo/errors/get_live_event_m3_u8_playback_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.live_event_m3_u8_playback.get_live_event_m3u8_playback_alt1

- **Route**: `GET /me/live_events/{live_event_id}/m3u8_playback`
- **Signature**: `def get_live_event_m3u8_playback_alt1(live_event_id: float, *, dvr: float | None = None, max_fps_fhd: float | None = None, ttl: float | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`
- **Params**: `live_event_id` — path · `dvr` — query · `max_fps_fhd` — query · `ttl` — query
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, GetLiveEventM3U8PlaybackAlt1ErrorBody]`
- **Error**: `GetLiveEventM3U8PlaybackAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401, 403, 404, 500, 503] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetLiveEventM3U8PlaybackAlt1ErrorBody` | `vimeo/errors/get_live_event_m3_u8_playback_alt1_error.py` |
| `Error` | `vimeo/models/error.py` |

