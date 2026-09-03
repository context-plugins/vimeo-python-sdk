<!-- Generated file — do not edit; regenerated with the SDK. -->

# SearchFederated — operations

Accessor: `client.search_federated` · Source: `vimeo_api/apis/search_federated.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.search_federated.federated_search_user_items

- **Route**: `GET /search/{user_id}/items`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def federated_search_user_items(user_id: float, *, direction: DirectionOrStr | None = None, filter: Filter30OrStr | None = None, filter_privacy: str | None = None, modified_end_date: str | None = None, modified_start_date: str | None = None, page: float | None = None, per_page: float | None = None, query: str | None = None, query_fields: str | None = None, sort: Sort46OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`
- **Params**: `user_id` — path · `direction` — query · `filter` — query · `filter_privacy` — query · `modified_end_date` — query · `modified_start_date` — query · `page` — query · `per_page` — query · `query` — query · `query_fields` — query · `sort` — query
- **Returns (parsed)**: `FederatedSearchItemsConnection`
- **Returns (raw)**: `ApiResult[FederatedSearchItemsConnection, FederatedSearchUserItemsErrorBody]`
- **Error**: `FederatedSearchUserItemsErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo_api/models/enums/direction.py` |
| `Filter30OrStr` | `vimeo_api/models/enums/filter30.py` |
| `Sort46OrStr` | `vimeo_api/models/enums/sort46.py` |
| `FederatedSearchItemsConnection` | `vimeo_api/models/federated_search_items_connection.py` |
| `FederatedSearchUserItemsErrorBody` | `vimeo_api/errors/federated_search_user_items_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.search_federated.federated_search_user_items_alt1

- **Route**: `GET /workspaces/search/{workspace_uuid}/items`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def federated_search_user_items_alt1(workspace_uuid: str, *, direction: DirectionOrStr | None = None, filter: Filter30OrStr | None = None, filter_privacy: str | None = None, modified_end_date: str | None = None, modified_start_date: str | None = None, page: float | None = None, per_page: float | None = None, query: str | None = None, query_fields: str | None = None, sort: Sort46OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `workspace_uuid`
- **Params**: `workspace_uuid` — path · `direction` — query · `filter` — query · `filter_privacy` — query · `modified_end_date` — query · `modified_start_date` — query · `page` — query · `per_page` — query · `query` — query · `query_fields` — query · `sort` — query
- **Returns (parsed)**: `FederatedSearchItemsConnection`
- **Returns (raw)**: `ApiResult[FederatedSearchItemsConnection, FederatedSearchUserItemsAlt1ErrorBody]`
- **Error**: `FederatedSearchUserItemsAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo_api/models/enums/direction.py` |
| `Filter30OrStr` | `vimeo_api/models/enums/filter30.py` |
| `Sort46OrStr` | `vimeo_api/models/enums/sort46.py` |
| `FederatedSearchItemsConnection` | `vimeo_api/models/federated_search_items_connection.py` |
| `FederatedSearchUserItemsAlt1ErrorBody` | `vimeo_api/errors/federated_search_user_items_alt1_error.py` |
| `Error` | `vimeo_api/models/error.py` |

