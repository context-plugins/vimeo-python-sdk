<!-- Generated file — do not edit; regenerated with the SDK. -->

# PortfoliosVideos — operations

Accessor: `client.portfolios_videos` · Source: `vimeo/apis/portfolios_videos.py` · 8 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.portfolios_videos.add_video_to_portfolio

- **Route**: `PUT /users/{user_id}/portfolios/{portfolio_id}/videos/{video_id}`
- **Signature**: `def add_video_to_portfolio(portfolio_id: float, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `portfolio_id`, `user_id`, `video_id`
- **Params**: `portfolio_id` — path · `user_id` — path · `video_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, AddVideoToPortfolioErrorBody]`
- **Error**: `AddVideoToPortfolioErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AddVideoToPortfolioErrorBody` | `vimeo/errors/add_video_to_portfolio_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.portfolios_videos.add_video_to_portfolio_alt1

- **Route**: `PUT /me/portfolios/{portfolio_id}/videos/{video_id}`
- **Signature**: `def add_video_to_portfolio_alt1(portfolio_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `portfolio_id`, `video_id`
- **Params**: `portfolio_id` — path · `video_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, AddVideoToPortfolioAlt1ErrorBody]`
- **Error**: `AddVideoToPortfolioAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AddVideoToPortfolioAlt1ErrorBody` | `vimeo/errors/add_video_to_portfolio_alt1_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.portfolios_videos.delete_video_from_portfolio

- **Route**: `DELETE /users/{user_id}/portfolios/{portfolio_id}/videos/{video_id}`
- **Signature**: `def delete_video_from_portfolio(portfolio_id: float, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `portfolio_id`, `user_id`, `video_id`
- **Params**: `portfolio_id` — path · `user_id` — path · `video_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteVideoFromPortfolioErrorBody]`
- **Error**: `DeleteVideoFromPortfolioErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteVideoFromPortfolioErrorBody` | `vimeo/errors/delete_video_from_portfolio_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.portfolios_videos.delete_video_from_portfolio_alt1

- **Route**: `DELETE /me/portfolios/{portfolio_id}/videos/{video_id}`
- **Signature**: `def delete_video_from_portfolio_alt1(portfolio_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `portfolio_id`, `video_id`
- **Params**: `portfolio_id` — path · `video_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteVideoFromPortfolioAlt1ErrorBody]`
- **Error**: `DeleteVideoFromPortfolioAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteVideoFromPortfolioAlt1ErrorBody` | `vimeo/errors/delete_video_from_portfolio_alt1_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.portfolios_videos.get_portfolio_video

- **Route**: `GET /users/{user_id}/portfolios/{portfolio_id}/videos/{video_id}`
- **Signature**: `def get_portfolio_video(portfolio_id: float, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `portfolio_id`, `user_id`, `video_id`
- **Params**: `portfolio_id` — path · `user_id` — path · `video_id` — path
- **Returns (parsed)**: `Video`
- **Returns (raw)**: `ApiResult[Video, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Video` | `vimeo/models/video.py` |

### client.portfolios_videos.get_portfolio_video_alt1

- **Route**: `GET /me/portfolios/{portfolio_id}/videos/{video_id}`
- **Signature**: `def get_portfolio_video_alt1(portfolio_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `portfolio_id`, `video_id`
- **Params**: `portfolio_id` — path · `video_id` — path
- **Returns (parsed)**: `Video`
- **Returns (raw)**: `ApiResult[Video, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Video` | `vimeo/models/video.py` |

### client.portfolios_videos.get_portfolio_videos

- **Route**: `GET /users/{user_id}/portfolios/{portfolio_id}/videos`
- **Signature**: `def get_portfolio_videos(portfolio_id: float, user_id: float, *, containing_uri: str | None = None, filter: Filter3OrStr | None = None, filter_embeddable: bool | None = None, page: float | None = None, per_page: float | None = None, sort: Sort35OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `portfolio_id`, `user_id`
- **Params**: `portfolio_id` — path · `user_id` — path · `containing_uri` — query · `filter` — query · `filter_embeddable` — query · `page` — query · `per_page` — query · `sort` — query
- **Returns (parsed)**: `VideoConnection`
- **Returns (raw)**: `ApiResult[VideoConnection, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Filter3OrStr` | `vimeo/models/enums/filter3.py` |
| `Sort35OrStr` | `vimeo/models/enums/sort35.py` |
| `VideoConnection` | `vimeo/models/video_connection.py` |

### client.portfolios_videos.get_portfolio_videos_alt1

- **Route**: `GET /me/portfolios/{portfolio_id}/videos`
- **Signature**: `def get_portfolio_videos_alt1(portfolio_id: float, *, containing_uri: str | None = None, filter: Filter3OrStr | None = None, filter_embeddable: bool | None = None, page: float | None = None, per_page: float | None = None, sort: Sort35OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `portfolio_id`
- **Params**: `portfolio_id` — path · `containing_uri` — query · `filter` — query · `filter_embeddable` — query · `page` — query · `per_page` — query · `sort` — query
- **Returns (parsed)**: `VideoConnection`
- **Returns (raw)**: `ApiResult[VideoConnection, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Filter3OrStr` | `vimeo/models/enums/filter3.py` |
| `Sort35OrStr` | `vimeo/models/enums/sort35.py` |
| `VideoConnection` | `vimeo/models/video_connection.py` |

