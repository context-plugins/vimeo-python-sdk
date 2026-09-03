<!-- Generated file — do not edit; regenerated with the SDK. -->

# TeamsEssentials — operations

Accessor: `client.teams_essentials` · Source: `vimeo_api/apis/teams_essentials.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.teams_essentials.backfill_team_custom_metadata

- **Route**: `POST /teams/{user_id}/custom_metadata/backfill`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def backfill_team_custom_metadata(user_id: float, body: TeamsCustomMetadataBackfillRequest | TeamsCustomMetadataBackfillRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`, `body`
- **Params**: `user_id` — path · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, BackfillTeamCustomMetadataErrorBody]`
- **Error**: `BackfillTeamCustomMetadataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400] · `LegacyError` [401, 403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TeamsCustomMetadataBackfillRequest` | `vimeo_api/models/teams_custom_metadata_backfill_request.py` |
| `TeamsCustomMetadataBackfillRequestDict` | `vimeo_api/models/teams_custom_metadata_backfill_request.py` |
| `BackfillTeamCustomMetadataErrorBody` | `vimeo_api/errors/backfill_team_custom_metadata_error.py` |
| `Error` | `vimeo_api/models/error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.teams_essentials.get_team_custom_metadata_incomplete_videos

- **Route**: `GET /teams/{user_id}/custom_metadata/incomplete_videos`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_team_custom_metadata_incomplete_videos(user_id: float, *, page: float | None = None, per_page: float | None = None, sort: Sort48OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`
- **Params**: `user_id` — path · `page` — query · `per_page` — query · `sort` — query
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, GetTeamCustomMetadataIncompleteVideosErrorBody]`
- **Error**: `GetTeamCustomMetadataIncompleteVideosErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400] · `LegacyError` [401, 403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Sort48OrStr` | `vimeo_api/models/enums/sort48.py` |
| `GetTeamCustomMetadataIncompleteVideosErrorBody` | `vimeo_api/errors/get_team_custom_metadata_incomplete_videos_error.py` |
| `Error` | `vimeo_api/models/error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.teams_essentials.get_team_custom_metadata_settings

- **Route**: `GET /teams/{user_id}/custom_metadata`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_team_custom_metadata_settings(user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`
- **Params**: `user_id` — path
- **Returns (parsed)**: `CustomMetadataSettingsConnection`
- **Returns (raw)**: `ApiResult[CustomMetadataSettingsConnection, GetTeamCustomMetadataSettingsErrorBody]`
- **Error**: `GetTeamCustomMetadataSettingsErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [401, 403] · `Error` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CustomMetadataSettingsConnection` | `vimeo_api/models/custom_metadata_settings_connection.py` |
| `GetTeamCustomMetadataSettingsErrorBody` | `vimeo_api/errors/get_team_custom_metadata_settings_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.teams_essentials.update_custom_metadata_field_options

- **Route**: `PATCH /teams/{user_id}/custom_metadata/options`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def update_custom_metadata_field_options(user_id: float, body: TeamsCustomMetadataOptionsRequest | TeamsCustomMetadataOptionsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`, `body`
- **Params**: `user_id` — path · `body` — JSON body
- **Returns (parsed)**: `CustomMetadataSettings`
- **Returns (raw)**: `ApiResult[CustomMetadataSettings, UpdateCustomMetadataFieldOptionsErrorBody]`
- **Error**: `UpdateCustomMetadataFieldOptionsErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400] · `LegacyError` [401, 403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TeamsCustomMetadataOptionsRequest` | `vimeo_api/models/teams_custom_metadata_options_request.py` |
| `TeamsCustomMetadataOptionsRequestDict` | `vimeo_api/models/teams_custom_metadata_options_request.py` |
| `CustomMetadataSettings` | `vimeo_api/models/custom_metadata_settings.py` |
| `UpdateCustomMetadataFieldOptionsErrorBody` | `vimeo_api/errors/update_custom_metadata_field_options_error.py` |
| `Error` | `vimeo_api/models/error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.teams_essentials.upsert_custom_metadata_settings

- **Route**: `POST /teams/{user_id}/custom_metadata`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def upsert_custom_metadata_settings(user_id: float, *, body: TeamsCustomMetadataRequest | TeamsCustomMetadataRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`
- **Params**: `user_id` — path · `body` — JSON body
- **Returns (parsed)**: `list[CustomMetadataSettings]`
- **Returns (raw)**: `ApiResult[list[CustomMetadataSettings], UpsertCustomMetadataSettingsErrorBody]`
- **Error**: `UpsertCustomMetadataSettingsErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400] · `LegacyError` [401, 403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TeamsCustomMetadataRequest` | `vimeo_api/models/teams_custom_metadata_request.py` |
| `TeamsCustomMetadataRequestDict` | `vimeo_api/models/teams_custom_metadata_request.py` |
| `CustomMetadataSettings` | `vimeo_api/models/custom_metadata_settings.py` |
| `UpsertCustomMetadataSettingsErrorBody` | `vimeo_api/errors/upsert_custom_metadata_settings_error.py` |
| `Error` | `vimeo_api/models/error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

