<!-- Generated file — do not edit; regenerated with the SDK. -->

# LiveEssentials — operations

Accessor: `client.live_essentials` · Source: `vimeo/apis/live_essentials.py` · 19 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.live_essentials.create_live_event

- **Route**: `POST /users/{user_id}/live_events`
- **Signature**: `def create_live_event(user_id: float, body: UsersLiveEventsRequest1 | UsersLiveEventsRequest1Dict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`, `body`
- **Params**: `user_id` — path · `body` — JSON body
- **Returns (parsed)**: `RecurringEvent`
- **Returns (raw)**: `ApiResult[RecurringEvent, CreateLiveEventErrorBody]`
- **Error**: `CreateLiveEventErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401, 403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UsersLiveEventsRequest1` | `vimeo/models/users_live_events_request1.py` |
| `UsersLiveEventsRequest1Dict` | `vimeo/models/users_live_events_request1.py` |
| `RecurringEvent` | `vimeo/models/recurring_event.py` |
| `CreateLiveEventErrorBody` | `vimeo/errors/create_live_event_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.live_essentials.create_live_event_alt1

- **Route**: `POST /live_events`
- **Signature**: `def create_live_event_alt1(body: LiveEventsRequest1 | LiveEventsRequest1Dict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `RecurringEvent`
- **Returns (raw)**: `ApiResult[RecurringEvent, CreateLiveEventAlt1ErrorBody]`
- **Error**: `CreateLiveEventAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401, 403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `LiveEventsRequest1` | `vimeo/models/live_events_request1.py` |
| `LiveEventsRequest1Dict` | `vimeo/models/live_events_request1.py` |
| `RecurringEvent` | `vimeo/models/recurring_event.py` |
| `CreateLiveEventAlt1ErrorBody` | `vimeo/errors/create_live_event_alt1_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.live_essentials.create_live_event_alt2

- **Route**: `POST /me/live_events`
- **Signature**: `def create_live_event_alt2(body: MeLiveEventsRequest1 | MeLiveEventsRequest1Dict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `RecurringEvent`
- **Returns (raw)**: `ApiResult[RecurringEvent, CreateLiveEventAlt2ErrorBody]`
- **Error**: `CreateLiveEventAlt2ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401, 403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `MeLiveEventsRequest1` | `vimeo/models/me_live_events_request1.py` |
| `MeLiveEventsRequest1Dict` | `vimeo/models/me_live_events_request1.py` |
| `RecurringEvent` | `vimeo/models/recurring_event.py` |
| `CreateLiveEventAlt2ErrorBody` | `vimeo/errors/create_live_event_alt2_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.live_essentials.delete_live_event

- **Route**: `DELETE /users/{user_id}/live_events/{live_event_id}`
- **Signature**: `def delete_live_event(live_event_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`, `user_id`
- **Params**: `live_event_id` — path · `user_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteLiveEventErrorBody]`
- **Error**: `DeleteLiveEventErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteLiveEventErrorBody` | `vimeo/errors/delete_live_event_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.live_essentials.delete_live_event_alt1

- **Route**: `DELETE /live_events/{live_event_id}`
- **Signature**: `def delete_live_event_alt1(live_event_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`
- **Params**: `live_event_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteLiveEventAlt1ErrorBody]`
- **Error**: `DeleteLiveEventAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteLiveEventAlt1ErrorBody` | `vimeo/errors/delete_live_event_alt1_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.live_essentials.delete_live_event_alt2

- **Route**: `DELETE /me/live_events/{live_event_id}`
- **Signature**: `def delete_live_event_alt2(live_event_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`
- **Params**: `live_event_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteLiveEventAlt2ErrorBody]`
- **Error**: `DeleteLiveEventAlt2ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteLiveEventAlt2ErrorBody` | `vimeo/errors/delete_live_event_alt2_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.live_essentials.delete_live_events

- **Route**: `DELETE /users/{user_id}/live_events`
- **Signature**: `def delete_live_events(user_id: float, body: UsersLiveEventsRequest | UsersLiveEventsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`, `body`
- **Params**: `user_id` — path · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteLiveEventsErrorBody]`
- **Error**: `DeleteLiveEventsErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UsersLiveEventsRequest` | `vimeo/models/users_live_events_request.py` |
| `UsersLiveEventsRequestDict` | `vimeo/models/users_live_events_request.py` |
| `DeleteLiveEventsErrorBody` | `vimeo/errors/delete_live_events_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.live_essentials.delete_live_events_alt1

- **Route**: `DELETE /live_events`
- **Signature**: `def delete_live_events_alt1(body: LiveEventsRequest | LiveEventsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteLiveEventsAlt1ErrorBody]`
- **Error**: `DeleteLiveEventsAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `LiveEventsRequest` | `vimeo/models/live_events_request.py` |
| `LiveEventsRequestDict` | `vimeo/models/live_events_request.py` |
| `DeleteLiveEventsAlt1ErrorBody` | `vimeo/errors/delete_live_events_alt1_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.live_essentials.delete_live_events_alt2

- **Route**: `DELETE /me/live_events`
- **Signature**: `def delete_live_events_alt2(body: MeLiveEventsRequest | MeLiveEventsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteLiveEventsAlt2ErrorBody]`
- **Error**: `DeleteLiveEventsAlt2ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `MeLiveEventsRequest` | `vimeo/models/me_live_events_request.py` |
| `MeLiveEventsRequestDict` | `vimeo/models/me_live_events_request.py` |
| `DeleteLiveEventsAlt2ErrorBody` | `vimeo/errors/delete_live_events_alt2_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.live_essentials.get_live_event

- **Route**: `GET /users/{user_id}/live_events/{live_event_id}`
- **Signature**: `def get_live_event(live_event_id: float, user_id: float, *, password: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`, `user_id`
- **Params**: `live_event_id` — path · `user_id` — path · `password` — query
- **Returns (parsed)**: `RecurringEvent`
- **Returns (raw)**: `ApiResult[RecurringEvent, GetLiveEventErrorBody]`
- **Error**: `GetLiveEventErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `RecurringEvent` | `vimeo/models/recurring_event.py` |
| `GetLiveEventErrorBody` | `vimeo/errors/get_live_event_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.live_essentials.get_live_event_alt1

- **Route**: `GET /live_events/{live_event_id}`
- **Signature**: `def get_live_event_alt1(live_event_id: float, *, password: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`
- **Params**: `live_event_id` — path · `password` — query
- **Returns (parsed)**: `RecurringEvent`
- **Returns (raw)**: `ApiResult[RecurringEvent, GetLiveEventAlt1ErrorBody]`
- **Error**: `GetLiveEventAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `RecurringEvent` | `vimeo/models/recurring_event.py` |
| `GetLiveEventAlt1ErrorBody` | `vimeo/errors/get_live_event_alt1_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.live_essentials.get_live_event_alt2

- **Route**: `GET /me/live_events/{live_event_id}`
- **Signature**: `def get_live_event_alt2(live_event_id: float, *, password: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`
- **Params**: `live_event_id` — path · `password` — query
- **Returns (parsed)**: `RecurringEvent`
- **Returns (raw)**: `ApiResult[RecurringEvent, GetLiveEventAlt2ErrorBody]`
- **Error**: `GetLiveEventAlt2ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `RecurringEvent` | `vimeo/models/recurring_event.py` |
| `GetLiveEventAlt2ErrorBody` | `vimeo/errors/get_live_event_alt2_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.live_essentials.get_live_event_occurrences

- **Route**: `GET /users/{user_id}/live_events_occurrences`
- **Signature**: `def get_live_event_occurrences(user_id: float, start_date: str, *, end_date: str | None = None, page: float | None = None, per_page: float | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`, `start_date`
- **Params**: `user_id` — path · `start_date` — query · `end_date` — query · `page` — query · `per_page` — query
- **Returns (parsed)**: `LiveEventOccurrenceConnection`
- **Returns (raw)**: `ApiResult[LiveEventOccurrenceConnection, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `LiveEventOccurrenceConnection` | `vimeo/models/live_event_occurrence_connection.py` |

### client.live_essentials.get_live_events

- **Route**: `GET /users/{user_id}/live_events`
- **Signature**: `def get_live_events(user_id: float, *, direction: DirectionOrStr | None = None, filter: Filter8OrStr | None = None, page: float | None = None, per_page: float | None = None, query: str | None = None, sort: Sort8OrStr | None = None, type_: Type31OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`
- **Params**: `user_id` — path · `direction` — query · `filter` — query · `page` — query · `per_page` — query · `query` — query · `sort` — query · `type_` — query `type`
- **Returns (parsed)**: `EventConnection`
- **Returns (raw)**: `ApiResult[EventConnection, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo/models/enums/direction.py` |
| `Filter8OrStr` | `vimeo/models/enums/filter8.py` |
| `Sort8OrStr` | `vimeo/models/enums/sort8.py` |
| `Type31OrStr` | `vimeo/models/enums/type31.py` |
| `EventConnection` | `vimeo/models/event_connection.py` |

### client.live_essentials.get_live_events_alt1

- **Route**: `GET /live_events`
- **Signature**: `def get_live_events_alt1(*, direction: DirectionOrStr | None = None, filter: Filter8OrStr | None = None, page: float | None = None, per_page: float | None = None, query: str | None = None, sort: Sort8OrStr | None = None, type_: Type31OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `direction` — query · `filter` — query · `page` — query · `per_page` — query · `query` — query · `sort` — query · `type_` — query `type`
- **Returns (parsed)**: `EventConnection`
- **Returns (raw)**: `ApiResult[EventConnection, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo/models/enums/direction.py` |
| `Filter8OrStr` | `vimeo/models/enums/filter8.py` |
| `Sort8OrStr` | `vimeo/models/enums/sort8.py` |
| `Type31OrStr` | `vimeo/models/enums/type31.py` |
| `EventConnection` | `vimeo/models/event_connection.py` |

### client.live_essentials.get_live_events_alt2

- **Route**: `GET /me/live_events`
- **Signature**: `def get_live_events_alt2(*, direction: DirectionOrStr | None = None, filter: Filter8OrStr | None = None, page: float | None = None, per_page: float | None = None, query: str | None = None, sort: Sort8OrStr | None = None, type_: Type31OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `direction` — query · `filter` — query · `page` — query · `per_page` — query · `query` — query · `sort` — query · `type_` — query `type`
- **Returns (parsed)**: `EventConnection`
- **Returns (raw)**: `ApiResult[EventConnection, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo/models/enums/direction.py` |
| `Filter8OrStr` | `vimeo/models/enums/filter8.py` |
| `Sort8OrStr` | `vimeo/models/enums/sort8.py` |
| `Type31OrStr` | `vimeo/models/enums/type31.py` |
| `EventConnection` | `vimeo/models/event_connection.py` |

### client.live_essentials.update_live_event

- **Route**: `PATCH /users/{user_id}/live_events/{live_event_id}`
- **Signature**: `def update_live_event(live_event_id: float, user_id: float, *, body: UsersLiveEventsRequest2 | UsersLiveEventsRequest2Dict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`, `user_id`
- **Params**: `live_event_id` — path · `user_id` — path · `body` — JSON body
- **Returns (parsed)**: `RecurringEvent`
- **Returns (raw)**: `ApiResult[RecurringEvent, UpdateLiveEventErrorBody]`
- **Error**: `UpdateLiveEventErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UsersLiveEventsRequest2` | `vimeo/models/users_live_events_request2.py` |
| `UsersLiveEventsRequest2Dict` | `vimeo/models/users_live_events_request2.py` |
| `RecurringEvent` | `vimeo/models/recurring_event.py` |
| `UpdateLiveEventErrorBody` | `vimeo/errors/update_live_event_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.live_essentials.update_live_event_alt1

- **Route**: `PATCH /live_events/{live_event_id}`
- **Signature**: `def update_live_event_alt1(live_event_id: float, *, body: LiveEventsRequest2 | LiveEventsRequest2Dict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`
- **Params**: `live_event_id` — path · `body` — JSON body
- **Returns (parsed)**: `RecurringEvent`
- **Returns (raw)**: `ApiResult[RecurringEvent, UpdateLiveEventAlt1ErrorBody]`
- **Error**: `UpdateLiveEventAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `LiveEventsRequest2` | `vimeo/models/live_events_request2.py` |
| `LiveEventsRequest2Dict` | `vimeo/models/live_events_request2.py` |
| `RecurringEvent` | `vimeo/models/recurring_event.py` |
| `UpdateLiveEventAlt1ErrorBody` | `vimeo/errors/update_live_event_alt1_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.live_essentials.update_live_event_alt2

- **Route**: `PATCH /me/live_events/{live_event_id}`
- **Signature**: `def update_live_event_alt2(live_event_id: float, *, body: MeLiveEventsRequest2 | MeLiveEventsRequest2Dict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`
- **Params**: `live_event_id` — path · `body` — JSON body
- **Returns (parsed)**: `RecurringEvent`
- **Returns (raw)**: `ApiResult[RecurringEvent, UpdateLiveEventAlt2ErrorBody]`
- **Error**: `UpdateLiveEventAlt2ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `MeLiveEventsRequest2` | `vimeo/models/me_live_events_request2.py` |
| `MeLiveEventsRequest2Dict` | `vimeo/models/me_live_events_request2.py` |
| `RecurringEvent` | `vimeo/models/recurring_event.py` |
| `UpdateLiveEventAlt2ErrorBody` | `vimeo/errors/update_live_event_alt2_error.py` |
| `Error` | `vimeo/models/error.py` |

