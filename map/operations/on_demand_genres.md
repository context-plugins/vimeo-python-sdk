<!-- Generated file — do not edit; regenerated with the SDK. -->

# OnDemandGenres — operations

Accessor: `client.on_demand_genres` · Source: `vimeo_api/apis/on_demand_genres.py` · 8 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.on_demand_genres.add_vod_genre

- **Route**: `PUT /ondemand/pages/{ondemand_id}/genres/{genre_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def add_vod_genre(genre_id: str, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `genre_id`, `ondemand_id`
- **Params**: `genre_id` — path · `ondemand_id` — path
- **Returns (parsed)**: `OnDemandGenre`
- **Returns (raw)**: `ApiResult[OnDemandGenre, AddVodGenreErrorBody]`
- **Error**: `AddVodGenreErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [400, 403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `OnDemandGenre` | `vimeo_api/models/on_demand_genre.py` |
| `AddVodGenreErrorBody` | `vimeo_api/errors/add_vod_genre_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.on_demand_genres.delete_vod_genre

- **Route**: `DELETE /ondemand/pages/{ondemand_id}/genres/{genre_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def delete_vod_genre(genre_id: str, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `genre_id`, `ondemand_id`
- **Params**: `genre_id` — path · `ondemand_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteVodGenreErrorBody]`
- **Error**: `DeleteVodGenreErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [400, 403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteVodGenreErrorBody` | `vimeo_api/errors/delete_vod_genre_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.on_demand_genres.get_genre_vod

- **Route**: `GET /ondemand/genres/{genre_id}/pages/{ondemand_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_genre_vod(genre_id: str, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `genre_id`, `ondemand_id`
- **Params**: `genre_id` — path · `ondemand_id` — path
- **Returns (parsed)**: `OnDemandPage`
- **Returns (raw)**: `ApiResult[OnDemandPage, GetGenreVodErrorBody]`
- **Error**: `GetGenreVodErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `OnDemandPage` | `vimeo_api/models/on_demand_page.py` |
| `GetGenreVodErrorBody` | `vimeo_api/errors/get_genre_vod_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.on_demand_genres.get_genre_vods

- **Route**: `GET /ondemand/genres/{genre_id}/pages`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_genre_vods(genre_id: str, *, direction: DirectionOrStr | None = None, filter_: Filter24OrStr | None = None, page: float | None = None, per_page: float | None = None, query: str | None = None, sort: Sort41OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `genre_id`
- **Params**: `genre_id` — path · `direction` — query · `filter_` — query `filter` · `page` — query · `per_page` — query · `query` — query · `sort` — query
- **Returns (parsed)**: `OnDemandPageConnection`
- **Returns (raw)**: `ApiResult[OnDemandPageConnection, GetGenreVodsErrorBody]`
- **Error**: `GetGenreVodsErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo_api/models/enums/direction.py` |
| `Filter24OrStr` | `vimeo_api/models/enums/filter24.py` |
| `Sort41OrStr` | `vimeo_api/models/enums/sort41.py` |
| `OnDemandPageConnection` | `vimeo_api/models/on_demand_page_connection.py` |
| `GetGenreVodsErrorBody` | `vimeo_api/errors/get_genre_vods_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.on_demand_genres.get_vod_genre

- **Route**: `GET /ondemand/genres/{genre_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_vod_genre(genre_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `genre_id`
- **Params**: `genre_id` — path
- **Returns (parsed)**: `OnDemandGenre`
- **Returns (raw)**: `ApiResult[OnDemandGenre, GetVodGenreErrorBody]`
- **Error**: `GetVodGenreErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `OnDemandGenre` | `vimeo_api/models/on_demand_genre.py` |
| `GetVodGenreErrorBody` | `vimeo_api/errors/get_vod_genre_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.on_demand_genres.get_vod_genre_by_ondemand_id

- **Route**: `GET /ondemand/pages/{ondemand_id}/genres/{genre_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_vod_genre_by_ondemand_id(genre_id: str, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `genre_id`, `ondemand_id`
- **Params**: `genre_id` — path · `ondemand_id` — path
- **Returns (parsed)**: `OnDemandGenre`
- **Returns (raw)**: `ApiResult[OnDemandGenre, GetVodGenreByOndemandIdErrorBody]`
- **Error**: `GetVodGenreByOndemandIdErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `OnDemandGenre` | `vimeo_api/models/on_demand_genre.py` |
| `GetVodGenreByOndemandIdErrorBody` | `vimeo_api/errors/get_vod_genre_by_ondemand_id_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.on_demand_genres.get_vod_genres

- **Route**: `GET /ondemand/genres`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_vod_genres(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `OnDemandGenreConnection`
- **Returns (raw)**: `ApiResult[OnDemandGenreConnection, GetVodGenresErrorBody]`
- **Error**: `GetVodGenresErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `OnDemandGenreConnection` | `vimeo_api/models/on_demand_genre_connection.py` |
| `GetVodGenresErrorBody` | `vimeo_api/errors/get_vod_genres_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.on_demand_genres.get_vod_genres_by_ondemand_id

- **Route**: `GET /ondemand/pages/{ondemand_id}/genres`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_vod_genres_by_ondemand_id(ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ondemand_id`
- **Params**: `ondemand_id` — path
- **Returns (parsed)**: `OnDemandGenreConnection`
- **Returns (raw)**: `ApiResult[OnDemandGenreConnection, GetVodGenresByOndemandIdErrorBody]`
- **Error**: `GetVodGenresByOndemandIdErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `OnDemandGenreConnection` | `vimeo_api/models/on_demand_genre_connection.py` |
| `GetVodGenresByOndemandIdErrorBody` | `vimeo_api/errors/get_vod_genres_by_ondemand_id_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

