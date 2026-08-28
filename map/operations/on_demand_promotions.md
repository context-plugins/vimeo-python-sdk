<!-- Generated file — do not edit; regenerated with the SDK. -->

# OnDemandPromotions — operations

Accessor: `client.on_demand_promotions` · Source: `vimeo/apis/on_demand_promotions.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.on_demand_promotions.create_vod_promotion

- **Route**: `POST /ondemand/pages/{ondemand_id}/promotions`
- **Signature**: `def create_vod_promotion(ondemand_id: float, body: OndemandPagesPromotionsRequest | OndemandPagesPromotionsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ondemand_id`, `body`
- **Params**: `ondemand_id` — path · `body` — JSON body
- **Returns (parsed)**: `OnDemandPromotion`
- **Returns (raw)**: `ApiResult[OnDemandPromotion, CreateVodPromotionErrorBody]`
- **Error**: `CreateVodPromotionErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [400, 403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `OndemandPagesPromotionsRequest` | `vimeo/models/ondemand_pages_promotions_request.py` |
| `OndemandPagesPromotionsRequestDict` | `vimeo/models/ondemand_pages_promotions_request.py` |
| `OnDemandPromotion` | `vimeo/models/on_demand_promotion.py` |
| `CreateVodPromotionErrorBody` | `vimeo/errors/create_vod_promotion_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.on_demand_promotions.delete_vod_promotion

- **Route**: `DELETE /ondemand/pages/{ondemand_id}/promotions/{promotion_id}`
- **Signature**: `def delete_vod_promotion(ondemand_id: float, promotion_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ondemand_id`, `promotion_id`
- **Params**: `ondemand_id` — path · `promotion_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteVodPromotionErrorBody]`
- **Error**: `DeleteVodPromotionErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteVodPromotionErrorBody` | `vimeo/errors/delete_vod_promotion_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.on_demand_promotions.get_vod_promotion

- **Route**: `GET /ondemand/pages/{ondemand_id}/promotions/{promotion_id}`
- **Signature**: `def get_vod_promotion(ondemand_id: float, promotion_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ondemand_id`, `promotion_id`
- **Params**: `ondemand_id` — path · `promotion_id` — path
- **Returns (parsed)**: `OnDemandPromotion`
- **Returns (raw)**: `ApiResult[OnDemandPromotion, GetVodPromotionErrorBody]`
- **Error**: `GetVodPromotionErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `OnDemandPromotion` | `vimeo/models/on_demand_promotion.py` |
| `GetVodPromotionErrorBody` | `vimeo/errors/get_vod_promotion_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.on_demand_promotions.get_vod_promotion_codes

- **Route**: `GET /ondemand/pages/{ondemand_id}/promotions/{promotion_id}/codes`
- **Signature**: `def get_vod_promotion_codes(ondemand_id: float, promotion_id: float, *, page: float | None = None, per_page: float | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ondemand_id`, `promotion_id`
- **Params**: `ondemand_id` — path · `promotion_id` — path · `page` — query · `per_page` — query
- **Returns (parsed)**: `OnDemandPromotionCode`
- **Returns (raw)**: `ApiResult[OnDemandPromotionCode, GetVodPromotionCodesErrorBody]`
- **Error**: `GetVodPromotionCodesErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `OnDemandPromotionCode` | `vimeo/models/on_demand_promotion_code.py` |
| `GetVodPromotionCodesErrorBody` | `vimeo/errors/get_vod_promotion_codes_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.on_demand_promotions.get_vod_promotions

- **Route**: `GET /ondemand/pages/{ondemand_id}/promotions`
- **Signature**: `def get_vod_promotions(ondemand_id: float, filter: Filter26OrStr, *, page: float | None = None, per_page: float | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ondemand_id`, `filter`
- **Params**: `ondemand_id` — path · `filter` — query · `page` — query · `per_page` — query
- **Returns (parsed)**: `OnDemandPromotion`
- **Returns (raw)**: `ApiResult[OnDemandPromotion, GetVodPromotionsErrorBody]`
- **Error**: `GetVodPromotionsErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [400, 403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Filter26OrStr` | `vimeo/models/enums/filter26.py` |
| `OnDemandPromotion` | `vimeo/models/on_demand_promotion.py` |
| `GetVodPromotionsErrorBody` | `vimeo/errors/get_vod_promotions_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

