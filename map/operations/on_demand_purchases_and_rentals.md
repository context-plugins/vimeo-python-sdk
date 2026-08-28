<!-- Generated file — do not edit; regenerated with the SDK. -->

# OnDemandPurchasesAndRentals — operations

Accessor: `client.on_demand_purchases_and_rentals` · Source: `vimeo/apis/on_demand_purchases_and_rentals.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.on_demand_purchases_and_rentals.check_if_vod_was_purchased_alt1

- **Route**: `GET /me/ondemand/purchases/{ondemand_id}`
- **Signature**: `def check_if_vod_was_purchased_alt1(ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ondemand_id`
- **Params**: `ondemand_id` — path
- **Returns (parsed)**: `OnDemandPage`
- **Returns (raw)**: `ApiResult[OnDemandPage, CheckIfVodWasPurchasedAlt1ErrorBody]`
- **Error**: `CheckIfVodWasPurchasedAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `OnDemandPage` | `vimeo/models/on_demand_page.py` |
| `CheckIfVodWasPurchasedAlt1ErrorBody` | `vimeo/errors/check_if_vod_was_purchased_alt1_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.on_demand_purchases_and_rentals.get_vod_purchases

- **Route**: `GET /users/{user_id}/ondemand/purchases`
- **Signature**: `def get_vod_purchases(user_id: float, *, direction: DirectionOrStr | None = None, filter: Filter19OrStr | None = None, page: float | None = None, per_page: float | None = None, sort: Sort33OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`
- **Params**: `user_id` — path · `direction` — query · `filter` — query · `page` — query · `per_page` — query · `sort` — query
- **Returns (parsed)**: `OnDemandPageConnection`
- **Returns (raw)**: `ApiResult[OnDemandPageConnection, GetVodPurchasesErrorBody]`
- **Error**: `GetVodPurchasesErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo/models/enums/direction.py` |
| `Filter19OrStr` | `vimeo/models/enums/filter19.py` |
| `Sort33OrStr` | `vimeo/models/enums/sort33.py` |
| `OnDemandPageConnection` | `vimeo/models/on_demand_page_connection.py` |
| `GetVodPurchasesErrorBody` | `vimeo/errors/get_vod_purchases_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.on_demand_purchases_and_rentals.get_vod_purchases_alt1

- **Route**: `GET /me/ondemand/purchases`
- **Signature**: `def get_vod_purchases_alt1(*, direction: DirectionOrStr | None = None, filter: Filter19OrStr | None = None, page: float | None = None, per_page: float | None = None, sort: Sort33OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `direction` — query · `filter` — query · `page` — query · `per_page` — query · `sort` — query
- **Returns (parsed)**: `OnDemandPageConnection`
- **Returns (raw)**: `ApiResult[OnDemandPageConnection, GetVodPurchasesAlt1ErrorBody]`
- **Error**: `GetVodPurchasesAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo/models/enums/direction.py` |
| `Filter19OrStr` | `vimeo/models/enums/filter19.py` |
| `Sort33OrStr` | `vimeo/models/enums/sort33.py` |
| `OnDemandPageConnection` | `vimeo/models/on_demand_page_connection.py` |
| `GetVodPurchasesAlt1ErrorBody` | `vimeo/errors/get_vod_purchases_alt1_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

