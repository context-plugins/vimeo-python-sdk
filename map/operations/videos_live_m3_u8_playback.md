<!-- Generated file — do not edit; regenerated with the SDK. -->

# VideosLiveM3U8Playback — operations

Accessor: `client.videos_live_m3_u8_playback` · Source: `vimeo/apis/videos_live_m3_u8_playback.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.videos_live_m3_u8_playback.get_one_time_event_m3u8_playback

- **Route**: `GET /users/{user_id}/videos/{video_id}/m3u8_playback`
- **Signature**: `def get_one_time_event_m3u8_playback(user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`, `video_id`
- **Params**: `user_id` — path · `video_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, GetOneTimeEventM3U8PlaybackErrorBody]`
- **Error**: `GetOneTimeEventM3U8PlaybackErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [401, 403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetOneTimeEventM3U8PlaybackErrorBody` | `vimeo/errors/get_one_time_event_m3_u8_playback_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.videos_live_m3_u8_playback.get_one_time_event_m3u8_playback_alt1

- **Route**: `GET /me/videos/{video_id}/m3u8_playback`
- **Signature**: `def get_one_time_event_m3u8_playback_alt1(video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, GetOneTimeEventM3U8PlaybackAlt1ErrorBody]`
- **Error**: `GetOneTimeEventM3U8PlaybackAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [401, 403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetOneTimeEventM3U8PlaybackAlt1ErrorBody` | `vimeo/errors/get_one_time_event_m3_u8_playback_alt1_error.py` |
| `Error` | `vimeo/models/error.py` |

