<!-- Generated file — do not edit; regenerated with the SDK. -->

# PortfoliosEssentials — operations

Accessor: `client.portfolios_essentials` · Source: `vimeo_api/apis/portfolios_essentials.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.portfolios_essentials.get_portfolio

- **Route**: `GET /users/{user_id}/portfolios/{portfolio_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_portfolio(portfolio_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `portfolio_id`, `user_id`
- **Params**: `portfolio_id` — path · `user_id` — path
- **Returns (parsed)**: `Portfolio`
- **Returns (raw)**: `ApiResult[Portfolio, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Portfolio` | `vimeo_api/models/portfolio.py` |

### client.portfolios_essentials.get_portfolio_alt1

- **Route**: `GET /me/portfolios/{portfolio_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_portfolio_alt1(portfolio_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `portfolio_id`
- **Params**: `portfolio_id` — path
- **Returns (parsed)**: `Portfolio`
- **Returns (raw)**: `ApiResult[Portfolio, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Portfolio` | `vimeo_api/models/portfolio.py` |

### client.portfolios_essentials.get_portfolios

- **Route**: `GET /users/{user_id}/portfolios`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_portfolios(user_id: float, *, direction: DirectionOrStr | None = None, page: float | None = None, per_page: float | None = None, query: str | None = None, sort: Sort8OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`
- **Params**: `user_id` — path · `direction` — query · `page` — query · `per_page` — query · `query` — query · `sort` — query
- **Returns (parsed)**: `PortfolioConnection`
- **Returns (raw)**: `ApiResult[PortfolioConnection, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo_api/models/enums/direction.py` |
| `Sort8OrStr` | `vimeo_api/models/enums/sort8.py` |
| `PortfolioConnection` | `vimeo_api/models/portfolio_connection.py` |

### client.portfolios_essentials.get_portfolios_alt1

- **Route**: `GET /me/portfolios`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_portfolios_alt1(*, direction: DirectionOrStr | None = None, page: float | None = None, per_page: float | None = None, query: str | None = None, sort: Sort8OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `direction` — query · `page` — query · `per_page` — query · `query` — query · `sort` — query
- **Returns (parsed)**: `PortfolioConnection`
- **Returns (raw)**: `ApiResult[PortfolioConnection, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo_api/models/enums/direction.py` |
| `Sort8OrStr` | `vimeo_api/models/enums/sort8.py` |
| `PortfolioConnection` | `vimeo_api/models/portfolio_connection.py` |

