<!-- Generated file — do not edit; regenerated with the SDK. -->

# LiveEventSessions — operations

Accessor: `client.live_event_sessions` · Source: `vimeo/apis/live_event_sessions.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.live_event_sessions.get_live_clip_ingest_status

- **Route**: `GET /live_events/{live_event_id}/session_status`
- **Signature**: `def get_live_clip_ingest_status(live_event_id: str, *, clip_id: float | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`
- **Params**: `live_event_id` — path · `clip_id` — query
- **Returns (parsed)**: `EventSessionStatus`
- **Returns (raw)**: `ApiResult[EventSessionStatus, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `EventSessionStatus` | `vimeo/models/event_session_status.py` |

### client.live_event_sessions.get_live_ingest_status

- **Route**: `GET /videos/{video_id}/sessions/status`
- **Signature**: `def get_live_ingest_status(video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path
- **Returns (parsed)**: `EventSessionStatus`
- **Returns (raw)**: `ApiResult[EventSessionStatus, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `EventSessionStatus` | `vimeo/models/event_session_status.py` |

