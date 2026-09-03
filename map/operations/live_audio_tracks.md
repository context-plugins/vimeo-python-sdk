<!-- Generated file — do not edit; regenerated with the SDK. -->

# LiveAudioTracks — operations

Accessor: `client.live_audio_tracks` · Source: `vimeo_api/apis/live_audio_tracks.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.live_audio_tracks.get_event_audio_tracks

- **Route**: `GET /live_events/{live_event_id}/audio_tracks`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_event_audio_tracks(live_event_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`
- **Params**: `live_event_id` — path
- **Returns (parsed)**: `EventAudioTracks`
- **Returns (raw)**: `ApiResult[EventAudioTracks, GetEventAudioTracksErrorBody]`
- **Error**: `GetEventAudioTracksErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [401, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `EventAudioTracks` | `vimeo_api/models/event_audio_tracks.py` |
| `GetEventAudioTracksErrorBody` | `vimeo_api/errors/get_event_audio_tracks_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.live_audio_tracks.update_event_audio_tracks

- **Route**: `PATCH /live_events/{live_event_id}/audio_tracks`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def update_event_audio_tracks(live_event_id: float, *, body: LiveEventsAudioTracksRequest | LiveEventsAudioTracksRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`
- **Params**: `live_event_id` — path · `body` — JSON body
- **Returns (parsed)**: `EventAudioTracks`
- **Returns (raw)**: `ApiResult[EventAudioTracks, UpdateEventAudioTracksErrorBody]`
- **Error**: `UpdateEventAudioTracksErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [401, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `LiveEventsAudioTracksRequest` | `vimeo_api/models/live_events_audio_tracks_request.py` |
| `LiveEventsAudioTracksRequestDict` | `vimeo_api/models/live_events_audio_tracks_request.py` |
| `EventAudioTracks` | `vimeo_api/models/event_audio_tracks.py` |
| `UpdateEventAudioTracksErrorBody` | `vimeo_api/errors/update_event_audio_tracks_error.py` |
| `Error` | `vimeo_api/models/error.py` |

