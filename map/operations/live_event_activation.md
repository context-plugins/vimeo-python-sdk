<!-- Generated file — do not edit; regenerated with the SDK. -->

# LiveEventActivation — operations

Accessor: `client.live_event_activation` · Source: `vimeo_api/apis/live_event_activation.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.live_event_activation.activate_live_event

- **Route**: `POST /users/{user_id}/live_events/{live_event_id}/activate`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def activate_live_event(live_event_id: float, user_id: float, *, body: UsersLiveEventsActivateRequest | UsersLiveEventsActivateRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`, `user_id`
- **Params**: `live_event_id` — path · `user_id` — path · `body` — JSON body
- **Returns (parsed)**: `Video`
- **Returns (raw)**: `ApiResult[Video, ActivateLiveEventErrorBody]`
- **Error**: `ActivateLiveEventErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401, 403, 404, 500, 503] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UsersLiveEventsActivateRequest` | `vimeo_api/models/users_live_events_activate_request.py` |
| `UsersLiveEventsActivateRequestDict` | `vimeo_api/models/users_live_events_activate_request.py` |
| `Video` | `vimeo_api/models/video.py` |
| `ActivateLiveEventErrorBody` | `vimeo_api/errors/activate_live_event_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.live_event_activation.activate_live_event_alt1

- **Route**: `POST /live_events/{live_event_id}/activate`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def activate_live_event_alt1(live_event_id: float, *, body: LiveEventsActivateRequest | LiveEventsActivateRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`
- **Params**: `live_event_id` — path · `body` — JSON body
- **Returns (parsed)**: `Video`
- **Returns (raw)**: `ApiResult[Video, ActivateLiveEventAlt1ErrorBody]`
- **Error**: `ActivateLiveEventAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401, 403, 404, 500, 503] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `LiveEventsActivateRequest` | `vimeo_api/models/live_events_activate_request.py` |
| `LiveEventsActivateRequestDict` | `vimeo_api/models/live_events_activate_request.py` |
| `Video` | `vimeo_api/models/video.py` |
| `ActivateLiveEventAlt1ErrorBody` | `vimeo_api/errors/activate_live_event_alt1_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.live_event_activation.activate_live_event_alt2

- **Route**: `POST /me/live_events/{live_event_id}/activate`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def activate_live_event_alt2(live_event_id: float, *, body: MeLiveEventsActivateRequest | MeLiveEventsActivateRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`
- **Params**: `live_event_id` — path · `body` — JSON body
- **Returns (parsed)**: `Video`
- **Returns (raw)**: `ApiResult[Video, ActivateLiveEventAlt2ErrorBody]`
- **Error**: `ActivateLiveEventAlt2ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401, 403, 404, 500, 503] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `MeLiveEventsActivateRequest` | `vimeo_api/models/me_live_events_activate_request.py` |
| `MeLiveEventsActivateRequestDict` | `vimeo_api/models/me_live_events_activate_request.py` |
| `Video` | `vimeo_api/models/video.py` |
| `ActivateLiveEventAlt2ErrorBody` | `vimeo_api/errors/activate_live_event_alt2_error.py` |
| `Error` | `vimeo_api/models/error.py` |

