<!-- Generated file — do not edit; regenerated with the SDK. -->

# LiveEventAutomatedClosedCaptions — operations

Accessor: `client.live_event_automated_closed_captions` · Source: `vimeo_api/apis/live_event_automated_closed_captions.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.live_event_automated_closed_captions.edit_live_event_auto_cc

- **Route**: `PATCH /users/{user_id}/live_events/{live_event_id}/auto_cc`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def edit_live_event_auto_cc(live_event_id: float, user_id: float, body: UsersLiveEventsAutoCcRequest | UsersLiveEventsAutoCcRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`, `user_id`, `body`
- **Params**: `live_event_id` — path · `user_id` — path · `body` — JSON body
- **Returns (parsed)**: `EventAutomatedClosedCaptions`
- **Returns (raw)**: `ApiResult[EventAutomatedClosedCaptions, EditLiveEventAutoCcErrorBody]`
- **Error**: `EditLiveEventAutoCcErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UsersLiveEventsAutoCcRequest` | `vimeo_api/models/users_live_events_auto_cc_request.py` |
| `UsersLiveEventsAutoCcRequestDict` | `vimeo_api/models/users_live_events_auto_cc_request.py` |
| `EventAutomatedClosedCaptions` | `vimeo_api/models/event_automated_closed_captions.py` |
| `EditLiveEventAutoCcErrorBody` | `vimeo_api/errors/edit_live_event_auto_cc_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.live_event_automated_closed_captions.edit_live_event_auto_cc_alt1

- **Route**: `PATCH /live_events/{live_event_id}/auto_cc`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def edit_live_event_auto_cc_alt1(live_event_id: float, body: LiveEventsAutoCcRequest | LiveEventsAutoCcRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`, `body`
- **Params**: `live_event_id` — path · `body` — JSON body
- **Returns (parsed)**: `EventAutomatedClosedCaptions`
- **Returns (raw)**: `ApiResult[EventAutomatedClosedCaptions, EditLiveEventAutoCcAlt1ErrorBody]`
- **Error**: `EditLiveEventAutoCcAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `LiveEventsAutoCcRequest` | `vimeo_api/models/live_events_auto_cc_request.py` |
| `LiveEventsAutoCcRequestDict` | `vimeo_api/models/live_events_auto_cc_request.py` |
| `EventAutomatedClosedCaptions` | `vimeo_api/models/event_automated_closed_captions.py` |
| `EditLiveEventAutoCcAlt1ErrorBody` | `vimeo_api/errors/edit_live_event_auto_cc_alt1_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.live_event_automated_closed_captions.edit_live_event_auto_cc_alt2

- **Route**: `PATCH /me/live_events/{live_event_id}/auto_cc`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def edit_live_event_auto_cc_alt2(live_event_id: float, body: MeLiveEventsAutoCcRequest | MeLiveEventsAutoCcRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`, `body`
- **Params**: `live_event_id` — path · `body` — JSON body
- **Returns (parsed)**: `EventAutomatedClosedCaptions`
- **Returns (raw)**: `ApiResult[EventAutomatedClosedCaptions, EditLiveEventAutoCcAlt2ErrorBody]`
- **Error**: `EditLiveEventAutoCcAlt2ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `MeLiveEventsAutoCcRequest` | `vimeo_api/models/me_live_events_auto_cc_request.py` |
| `MeLiveEventsAutoCcRequestDict` | `vimeo_api/models/me_live_events_auto_cc_request.py` |
| `EventAutomatedClosedCaptions` | `vimeo_api/models/event_automated_closed_captions.py` |
| `EditLiveEventAutoCcAlt2ErrorBody` | `vimeo_api/errors/edit_live_event_auto_cc_alt2_error.py` |
| `Error` | `vimeo_api/models/error.py` |

