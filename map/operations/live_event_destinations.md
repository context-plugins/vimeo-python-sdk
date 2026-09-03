<!-- Generated file — do not edit; regenerated with the SDK. -->

# LiveEventDestinations — operations

Accessor: `client.live_event_destinations` · Source: `vimeo_api/apis/live_event_destinations.py` · 12 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.live_event_destinations.create_live_event_destination

- **Route**: `POST /me/live_events/{live_event_id}/destinations`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def create_live_event_destination(live_event_id: float, body: MeLiveEventsDestinationsRequest | MeLiveEventsDestinationsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`, `body`
- **Params**: `live_event_id` — path · `body` — JSON body
- **Returns (parsed)**: `EventDestination`
- **Returns (raw)**: `ApiResult[EventDestination, CreateLiveEventDestinationErrorBody]`
- **Error**: `CreateLiveEventDestinationErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401, 403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `MeLiveEventsDestinationsRequest` | `vimeo_api/models/me_live_events_destinations_request.py` |
| `MeLiveEventsDestinationsRequestDict` | `vimeo_api/models/me_live_events_destinations_request.py` |
| `EventDestination` | `vimeo_api/models/event_destination.py` |
| `CreateLiveEventDestinationErrorBody` | `vimeo_api/errors/create_live_event_destination_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.live_event_destinations.create_live_event_destination_alt1

- **Route**: `POST /users/{user_id}/live_events/{live_event_id}/destinations`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def create_live_event_destination_alt1(live_event_id: float, user_id: float, body: UsersLiveEventsDestinationsRequest | UsersLiveEventsDestinationsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`, `user_id`, `body`
- **Params**: `live_event_id` — path · `user_id` — path · `body` — JSON body
- **Returns (parsed)**: `EventDestination`
- **Returns (raw)**: `ApiResult[EventDestination, CreateLiveEventDestinationAlt1ErrorBody]`
- **Error**: `CreateLiveEventDestinationAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401, 403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UsersLiveEventsDestinationsRequest` | `vimeo_api/models/users_live_events_destinations_request.py` |
| `UsersLiveEventsDestinationsRequestDict` | `vimeo_api/models/users_live_events_destinations_request.py` |
| `EventDestination` | `vimeo_api/models/event_destination.py` |
| `CreateLiveEventDestinationAlt1ErrorBody` | `vimeo_api/errors/create_live_event_destination_alt1_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.live_event_destinations.create_ott_destination

- **Route**: `POST /users/{user_id}/live_events/{live_event_id}/ott_destinations`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def create_ott_destination(live_event_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`, `user_id`
- **Params**: `live_event_id` — path · `user_id` — path
- **Returns (parsed)**: `OttDestination`
- **Returns (raw)**: `ApiResult[OttDestination, CreateOttDestinationErrorBody]`
- **Error**: `CreateOttDestinationErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401, 403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `OttDestination` | `vimeo_api/models/ott_destination.py` |
| `CreateOttDestinationErrorBody` | `vimeo_api/errors/create_ott_destination_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.live_event_destinations.delete_live_event_destination

- **Route**: `DELETE /destination/{destination_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def delete_live_event_destination(destination_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `destination_id`
- **Params**: `destination_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteLiveEventDestinationErrorBody]`
- **Error**: `DeleteLiveEventDestinationErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [401, 403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteLiveEventDestinationErrorBody` | `vimeo_api/errors/delete_live_event_destination_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.live_event_destinations.delete_ott_destination

- **Route**: `DELETE /users/{user_id}/live_events/{live_event_id}/ott_destination/{destination_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def delete_ott_destination(live_event_id: float, user_id: float, destination_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`, `user_id`, `destination_id`
- **Params**: `live_event_id` — path · `user_id` — path · `destination_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteOttDestinationErrorBody]`
- **Error**: `DeleteOttDestinationErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401, 403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteOttDestinationErrorBody` | `vimeo_api/errors/delete_ott_destination_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.live_event_destinations.get_available_destinations

- **Route**: `GET /users/{user_id}/destinations`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_available_destinations(user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`
- **Params**: `user_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, GetAvailableDestinationsErrorBody]`
- **Error**: `GetAvailableDestinationsErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [401, 403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetAvailableDestinationsErrorBody` | `vimeo_api/errors/get_available_destinations_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.live_event_destinations.get_available_destinations_alt1

- **Route**: `GET /me/destinations`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_available_destinations_alt1(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, GetAvailableDestinationsAlt1ErrorBody]`
- **Error**: `GetAvailableDestinationsAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [401, 403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetAvailableDestinationsAlt1ErrorBody` | `vimeo_api/errors/get_available_destinations_alt1_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.live_event_destinations.get_live_event_destination

- **Route**: `GET /destination/{destination_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_live_event_destination(destination_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `destination_id`
- **Params**: `destination_id` — path
- **Returns (parsed)**: `EventDestination`
- **Returns (raw)**: `ApiResult[EventDestination, GetLiveEventDestinationErrorBody]`
- **Error**: `GetLiveEventDestinationErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [401, 403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `EventDestination` | `vimeo_api/models/event_destination.py` |
| `GetLiveEventDestinationErrorBody` | `vimeo_api/errors/get_live_event_destination_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.live_event_destinations.get_live_event_destinations

- **Route**: `GET /me/live_events/{live_event_id}/destinations`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_live_event_destinations(live_event_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`
- **Params**: `live_event_id` — path
- **Returns (parsed)**: `EventDestinationConnection`
- **Returns (raw)**: `ApiResult[EventDestinationConnection, GetLiveEventDestinationsErrorBody]`
- **Error**: `GetLiveEventDestinationsErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401, 403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `EventDestinationConnection` | `vimeo_api/models/event_destination_connection.py` |
| `GetLiveEventDestinationsErrorBody` | `vimeo_api/errors/get_live_event_destinations_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.live_event_destinations.get_live_event_destinations_alt1

- **Route**: `GET /users/{user_id}/live_events/{live_event_id}/destinations`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_live_event_destinations_alt1(live_event_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`, `user_id`
- **Params**: `live_event_id` — path · `user_id` — path
- **Returns (parsed)**: `EventDestinationConnection`
- **Returns (raw)**: `ApiResult[EventDestinationConnection, GetLiveEventDestinationsAlt1ErrorBody]`
- **Error**: `GetLiveEventDestinationsAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401, 403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `EventDestinationConnection` | `vimeo_api/models/event_destination_connection.py` |
| `GetLiveEventDestinationsAlt1ErrorBody` | `vimeo_api/errors/get_live_event_destinations_alt1_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.live_event_destinations.get_ott_destinations

- **Route**: `GET /users/{user_id}/live_events/{live_event_id}/ott_destinations`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_ott_destinations(live_event_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`, `user_id`
- **Params**: `live_event_id` — path · `user_id` — path
- **Returns (parsed)**: `OttDestinationConnection`
- **Returns (raw)**: `ApiResult[OttDestinationConnection, GetOttDestinationsErrorBody]`
- **Error**: `GetOttDestinationsErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [401, 403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `OttDestinationConnection` | `vimeo_api/models/ott_destination_connection.py` |
| `GetOttDestinationsErrorBody` | `vimeo_api/errors/get_ott_destinations_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.live_event_destinations.update_live_event_destination

- **Route**: `PATCH /destination/{destination_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def update_live_event_destination(destination_id: float, *, body: DestinationRequest | DestinationRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `destination_id`
- **Params**: `destination_id` — path · `body` — JSON body
- **Returns (parsed)**: `EventDestination`
- **Returns (raw)**: `ApiResult[EventDestination, UpdateLiveEventDestinationErrorBody]`
- **Error**: `UpdateLiveEventDestinationErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401, 403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DestinationRequest` | `vimeo_api/models/destination_request.py` |
| `DestinationRequestDict` | `vimeo_api/models/destination_request.py` |
| `EventDestination` | `vimeo_api/models/event_destination.py` |
| `UpdateLiveEventDestinationErrorBody` | `vimeo_api/errors/update_live_event_destination_error.py` |
| `Error` | `vimeo_api/models/error.py` |

