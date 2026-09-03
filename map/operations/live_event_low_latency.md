<!-- Generated file — do not edit; regenerated with the SDK. -->

# LiveEventLowLatency — operations

Accessor: `client.live_event_low_latency` · Source: `vimeo_api/apis/live_event_low_latency.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.live_event_low_latency.toggle_rle_low_latency

- **Route**: `PATCH /users/{user_id}/live_events/{live_event_id}/low_latency`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def toggle_rle_low_latency(live_event_id: float, user_id: float, *, body: UsersLiveEventsLowLatencyRequest | UsersLiveEventsLowLatencyRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`, `user_id`
- **Params**: `live_event_id` — path · `user_id` — path · `body` — JSON body
- **Returns (parsed)**: `RecurringEventLowLatency`
- **Returns (raw)**: `ApiResult[RecurringEventLowLatency, ToggleRleLowLatencyErrorBody]`
- **Error**: `ToggleRleLowLatencyErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UsersLiveEventsLowLatencyRequest` | `vimeo_api/models/users_live_events_low_latency_request.py` |
| `UsersLiveEventsLowLatencyRequestDict` | `vimeo_api/models/users_live_events_low_latency_request.py` |
| `RecurringEventLowLatency` | `vimeo_api/models/recurring_event_low_latency.py` |
| `ToggleRleLowLatencyErrorBody` | `vimeo_api/errors/toggle_rle_low_latency_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.live_event_low_latency.toggle_rle_low_latency_alt1

- **Route**: `PATCH /live_events/{live_event_id}/low_latency`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def toggle_rle_low_latency_alt1(live_event_id: float, *, body: LiveEventsLowLatencyRequest | LiveEventsLowLatencyRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`
- **Params**: `live_event_id` — path · `body` — JSON body
- **Returns (parsed)**: `RecurringEventLowLatency`
- **Returns (raw)**: `ApiResult[RecurringEventLowLatency, ToggleRleLowLatencyAlt1ErrorBody]`
- **Error**: `ToggleRleLowLatencyAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `LiveEventsLowLatencyRequest` | `vimeo_api/models/live_events_low_latency_request.py` |
| `LiveEventsLowLatencyRequestDict` | `vimeo_api/models/live_events_low_latency_request.py` |
| `RecurringEventLowLatency` | `vimeo_api/models/recurring_event_low_latency.py` |
| `ToggleRleLowLatencyAlt1ErrorBody` | `vimeo_api/errors/toggle_rle_low_latency_alt1_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.live_event_low_latency.toggle_rle_low_latency_alt2

- **Route**: `PATCH /me/live_events/{live_event_id}/low_latency`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def toggle_rle_low_latency_alt2(live_event_id: float, *, body: MeLiveEventsLowLatencyRequest | MeLiveEventsLowLatencyRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`
- **Params**: `live_event_id` — path · `body` — JSON body
- **Returns (parsed)**: `RecurringEventLowLatency`
- **Returns (raw)**: `ApiResult[RecurringEventLowLatency, ToggleRleLowLatencyAlt2ErrorBody]`
- **Error**: `ToggleRleLowLatencyAlt2ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `MeLiveEventsLowLatencyRequest` | `vimeo_api/models/me_live_events_low_latency_request.py` |
| `MeLiveEventsLowLatencyRequestDict` | `vimeo_api/models/me_live_events_low_latency_request.py` |
| `RecurringEventLowLatency` | `vimeo_api/models/recurring_event_low_latency.py` |
| `ToggleRleLowLatencyAlt2ErrorBody` | `vimeo_api/errors/toggle_rle_low_latency_alt2_error.py` |
| `Error` | `vimeo_api/models/error.py` |

