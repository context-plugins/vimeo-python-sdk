<!-- Generated file — do not edit; regenerated with the SDK. -->

# ChannelsTags — operations

Accessor: `client.channels_tags` · Source: `vimeo_api/apis/channels_tags.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.channels_tags.add_channel_tag

- **Route**: `PUT /channels/{channel_id}/tags/{word}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def add_channel_tag(channel_id: float, word: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel_id`, `word`
- **Params**: `channel_id` — path · `word` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, AddChannelTagErrorBody]`
- **Error**: `AddChannelTagErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [400] · `Error` [401, 403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AddChannelTagErrorBody` | `vimeo_api/errors/add_channel_tag_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.channels_tags.add_tags_to_channel

- **Route**: `PUT /channels/{channel_id}/tags`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def add_tags_to_channel(channel_id: float, body: list[ChannelsTagsRequest | ChannelsTagsRequestDict], *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel_id`, `body`
- **Params**: `channel_id` — path · `body` — JSON body
- **Returns (parsed)**: `list[TagModel]`
- **Returns (raw)**: `ApiResult[list[TagModel], AddTagsToChannelErrorBody]`
- **Error**: `AddTagsToChannelErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [400] · `Error` [401, 403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ChannelsTagsRequest` | `vimeo_api/models/channels_tags_request.py` |
| `ChannelsTagsRequestDict` | `vimeo_api/models/channels_tags_request.py` |
| `TagModel` | `vimeo_api/models/tag_model.py` |
| `AddTagsToChannelErrorBody` | `vimeo_api/errors/add_tags_to_channel_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.channels_tags.check_if_channel_has_tag

- **Route**: `GET /channels/{channel_id}/tags/{word}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def check_if_channel_has_tag(channel_id: float, word: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel_id`, `word`
- **Params**: `channel_id` — path · `word` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, CheckIfChannelHasTagErrorBody]`
- **Error**: `CheckIfChannelHasTagErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [400] · `Error` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CheckIfChannelHasTagErrorBody` | `vimeo_api/errors/check_if_channel_has_tag_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.channels_tags.delete_tag_from_channel

- **Route**: `DELETE /channels/{channel_id}/tags/{word}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def delete_tag_from_channel(channel_id: float, word: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel_id`, `word`
- **Params**: `channel_id` — path · `word` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteTagFromChannelErrorBody]`
- **Error**: `DeleteTagFromChannelErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [400] · `Error` [401, 403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteTagFromChannelErrorBody` | `vimeo_api/errors/delete_tag_from_channel_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.channels_tags.get_channel_tags

- **Route**: `GET /channels/{channel_id}/tags`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_channel_tags(channel_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel_id`
- **Params**: `channel_id` — path
- **Returns (parsed)**: `TagConnection`
- **Returns (raw)**: `ApiResult[TagConnection, GetChannelTagsErrorBody]`
- **Error**: `GetChannelTagsErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TagConnection` | `vimeo_api/models/tag_connection.py` |
| `GetChannelTagsErrorBody` | `vimeo_api/errors/get_channel_tags_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

