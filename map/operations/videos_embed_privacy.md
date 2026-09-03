<!-- Generated file — do not edit; regenerated with the SDK. -->

# VideosEmbedPrivacy — operations

Accessor: `client.videos_embed_privacy` · Source: `vimeo_api/apis/videos_embed_privacy.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.videos_embed_privacy.add_video_privacy_domain

- **Route**: `PUT /videos/{video_id}/privacy/domains/{domain}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def add_video_privacy_domain(domain: str, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `domain`, `video_id`
- **Params**: `domain` — path · `video_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, AddVideoPrivacyDomainErrorBody]`
- **Error**: `AddVideoPrivacyDomainErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AddVideoPrivacyDomainErrorBody` | `vimeo_api/errors/add_video_privacy_domain_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.videos_embed_privacy.delete_video_privacy_domain

- **Route**: `DELETE /videos/{video_id}/privacy/domains/{domain}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def delete_video_privacy_domain(domain: str, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `domain`, `video_id`
- **Params**: `domain` — path · `video_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteVideoPrivacyDomainErrorBody]`
- **Error**: `DeleteVideoPrivacyDomainErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteVideoPrivacyDomainErrorBody` | `vimeo_api/errors/delete_video_privacy_domain_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.videos_embed_privacy.get_video_privacy_domains

- **Route**: `GET /videos/{video_id}/privacy/domains`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_video_privacy_domains(video_id: float, *, direction: DirectionOrStr | None = None, page: float | None = None, per_page: float | None = None, sort: Sort78OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path · `direction` — query · `page` — query · `per_page` — query · `sort` — query
- **Returns (parsed)**: `DomainConnection`
- **Returns (raw)**: `ApiResult[DomainConnection, GetVideoPrivacyDomainsErrorBody]`
- **Error**: `GetVideoPrivacyDomainsErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo_api/models/enums/direction.py` |
| `Sort78OrStr` | `vimeo_api/models/enums/sort78.py` |
| `DomainConnection` | `vimeo_api/models/domain_connection.py` |
| `GetVideoPrivacyDomainsErrorBody` | `vimeo_api/errors/get_video_privacy_domains_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

