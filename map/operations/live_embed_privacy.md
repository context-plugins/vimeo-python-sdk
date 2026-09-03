<!-- Generated file — do not edit; regenerated with the SDK. -->

# LiveEmbedPrivacy — operations

Accessor: `client.live_embed_privacy` · Source: `vimeo_api/apis/live_embed_privacy.py` · 6 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.live_embed_privacy.get_live_event_whitelist

- **Route**: `GET /users/{user_id}/live_events/{live_event_id}/privacy/domains`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_live_event_whitelist(live_event_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`, `user_id`
- **Params**: `live_event_id` — path · `user_id` — path
- **Returns (parsed)**: `DomainConnection`
- **Returns (raw)**: `ApiResult[DomainConnection, GetLiveEventWhitelistErrorBody]`
- **Error**: `GetLiveEventWhitelistErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 403, 404, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DomainConnection` | `vimeo_api/models/domain_connection.py` |
| `GetLiveEventWhitelistErrorBody` | `vimeo_api/errors/get_live_event_whitelist_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.live_embed_privacy.get_live_event_whitelist_alt1

- **Route**: `GET /live_events/{live_event_id}/privacy/domains`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_live_event_whitelist_alt1(live_event_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`
- **Params**: `live_event_id` — path
- **Returns (parsed)**: `DomainConnection`
- **Returns (raw)**: `ApiResult[DomainConnection, GetLiveEventWhitelistAlt1ErrorBody]`
- **Error**: `GetLiveEventWhitelistAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 403, 404, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DomainConnection` | `vimeo_api/models/domain_connection.py` |
| `GetLiveEventWhitelistAlt1ErrorBody` | `vimeo_api/errors/get_live_event_whitelist_alt1_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.live_embed_privacy.get_live_event_whitelist_alt2

- **Route**: `GET /me/live_events/{live_event_id}/privacy/domains`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_live_event_whitelist_alt2(live_event_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`
- **Params**: `live_event_id` — path
- **Returns (parsed)**: `DomainConnection`
- **Returns (raw)**: `ApiResult[DomainConnection, GetLiveEventWhitelistAlt2ErrorBody]`
- **Error**: `GetLiveEventWhitelistAlt2ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 403, 404, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DomainConnection` | `vimeo_api/models/domain_connection.py` |
| `GetLiveEventWhitelistAlt2ErrorBody` | `vimeo_api/errors/get_live_event_whitelist_alt2_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.live_embed_privacy.set_live_event_whitelist

- **Route**: `PUT /users/{user_id}/live_events/{live_event_id}/privacy/domains`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def set_live_event_whitelist(live_event_id: float, user_id: float, *, body: UsersLiveEventsPrivacyDomainsRequest | UsersLiveEventsPrivacyDomainsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`, `user_id`
- **Params**: `live_event_id` — path · `user_id` — path · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, SetLiveEventWhitelistErrorBody]`
- **Error**: `SetLiveEventWhitelistErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 403, 404, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UsersLiveEventsPrivacyDomainsRequest` | `vimeo_api/models/users_live_events_privacy_domains_request.py` |
| `UsersLiveEventsPrivacyDomainsRequestDict` | `vimeo_api/models/users_live_events_privacy_domains_request.py` |
| `SetLiveEventWhitelistErrorBody` | `vimeo_api/errors/set_live_event_whitelist_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.live_embed_privacy.set_live_event_whitelist_alt1

- **Route**: `PUT /live_events/{live_event_id}/privacy/domains`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def set_live_event_whitelist_alt1(live_event_id: float, *, body: LiveEventsPrivacyDomainsRequest | LiveEventsPrivacyDomainsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`
- **Params**: `live_event_id` — path · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, SetLiveEventWhitelistAlt1ErrorBody]`
- **Error**: `SetLiveEventWhitelistAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 403, 404, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `LiveEventsPrivacyDomainsRequest` | `vimeo_api/models/live_events_privacy_domains_request.py` |
| `LiveEventsPrivacyDomainsRequestDict` | `vimeo_api/models/live_events_privacy_domains_request.py` |
| `SetLiveEventWhitelistAlt1ErrorBody` | `vimeo_api/errors/set_live_event_whitelist_alt1_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.live_embed_privacy.set_live_event_whitelist_alt2

- **Route**: `PUT /me/live_events/{live_event_id}/privacy/domains`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def set_live_event_whitelist_alt2(live_event_id: float, *, body: MeLiveEventsPrivacyDomainsRequest | MeLiveEventsPrivacyDomainsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`
- **Params**: `live_event_id` — path · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, SetLiveEventWhitelistAlt2ErrorBody]`
- **Error**: `SetLiveEventWhitelistAlt2ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 403, 404, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `MeLiveEventsPrivacyDomainsRequest` | `vimeo_api/models/me_live_events_privacy_domains_request.py` |
| `MeLiveEventsPrivacyDomainsRequestDict` | `vimeo_api/models/me_live_events_privacy_domains_request.py` |
| `SetLiveEventWhitelistAlt2ErrorBody` | `vimeo_api/errors/set_live_event_whitelist_alt2_error.py` |
| `Error` | `vimeo_api/models/error.py` |

