<!-- Generated file — do not edit; regenerated with the SDK. -->

# FilesRemote — operations

Accessor: `client.files_remote` · Source: `slack_web_api/apis/files_remote.py` · 6 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.files_remote.files_remote_add

- **Route**: `POST /files.remote.add`
- **Signature**: `def files_remote_add(content_type: ContentTypeOrStr, *, token: str | None = None, external_id: str | None = None, title: str | None = None, filetype: str | None = None, external_url: str | None = None, preview_image: str | None = None, indexable_file_contents: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`
- **Params**: `content_type` — header `Content-Type` · `token` — form field · `external_id` — form field · `title` — form field · `filetype` — form field · `external_url` — form field · `preview_image` — form field · `indexable_file_contents` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.files_remote.files_remote_info

- **Route**: `GET /files.remote.info`
- **Signature**: `def files_remote_info(content_type: ContentTypeOrStr, *, token: str | None = None, file: str | None = None, external_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`
- **Params**: `token` — query · `file` — query · `external_id` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.files_remote.files_remote_list

- **Route**: `GET /files.remote.list`
- **Signature**: `def files_remote_list(content_type: ContentTypeOrStr, *, token: str | None = None, channel: str | None = None, ts_from: float | None = None, ts_to: float | None = None, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`
- **Params**: `token` — query · `channel` — query · `ts_from` — query · `ts_to` — query · `limit` — query · `cursor` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.files_remote.files_remote_remove

- **Route**: `POST /files.remote.remove`
- **Signature**: `def files_remote_remove(content_type: ContentTypeOrStr, *, token: str | None = None, file: str | None = None, external_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`
- **Params**: `content_type` — header `Content-Type` · `token` — form field · `file` — form field · `external_id` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.files_remote.files_remote_share

- **Route**: `GET /files.remote.share`
- **Signature**: `def files_remote_share(content_type: ContentTypeOrStr, *, token: str | None = None, file: str | None = None, external_id: str | None = None, channels: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`
- **Params**: `token` — query · `file` — query · `external_id` — query · `channels` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.files_remote.files_remote_update

- **Route**: `POST /files.remote.update`
- **Signature**: `def files_remote_update(content_type: ContentTypeOrStr, *, token: str | None = None, file: str | None = None, external_id: str | None = None, title: str | None = None, filetype: str | None = None, external_url: str | None = None, preview_image: str | None = None, indexable_file_contents: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`
- **Params**: `content_type` — header `Content-Type` · `token` — form field · `file` — form field · `external_id` — form field · `title` — form field · `filetype` — form field · `external_url` — form field · `preview_image` — form field · `indexable_file_contents` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

