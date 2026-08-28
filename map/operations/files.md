<!-- Generated file — do not edit; regenerated with the SDK. -->

# Files — operations

Accessor: `client.files` · Source: `slack_web_api/apis/files.py` · 13 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.files.files_comments_delete

- **Route**: `POST /files.comments.delete`
- **Signature**: `def files_comments_delete(content_type: ContentTypeOrStr, *, token: str | None = None, file: str | None = None, id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`
- **Params**: `content_type` — header `Content-Type` · `token` — header · `file` — form field · `id` — form field
- **Returns (parsed)**: `FilesCommentsDeleteschema`
- **Returns (raw)**: `ApiResult[FilesCommentsDeleteschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `FilesCommentsDeleteschema` | `slack_web_api/models/files_comments_deleteschema.py` |

### client.files.files_delete

- **Route**: `POST /files.delete`
- **Signature**: `def files_delete(content_type: ContentTypeOrStr, *, token: str | None = None, file: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`
- **Params**: `content_type` — header `Content-Type` · `token` — header · `file` — form field
- **Returns (parsed)**: `FilesDeleteschema`
- **Returns (raw)**: `ApiResult[FilesDeleteschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `FilesDeleteschema` | `slack_web_api/models/files_deleteschema.py` |

### client.files.files_info

- **Route**: `GET /files.info`
- **Signature**: `def files_info(content_type: ContentTypeOrStr, *, token: str | None = None, file: str | None = None, count: str | None = None, page: str | None = None, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`
- **Params**: `token` — query · `file` — query · `count` — query · `page` — query · `limit` — query · `cursor` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `FilesInfoschema`
- **Returns (raw)**: `ApiResult[FilesInfoschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `FilesInfoschema` | `slack_web_api/models/files_infoschema.py` |

### client.files.files_list

- **Route**: `GET /files.list`
- **Signature**: `def files_list(content_type: ContentTypeOrStr, *, token: str | None = None, user: str | None = None, channel: str | None = None, ts_from: float | None = None, ts_to: float | None = None, types: str | None = None, count: str | None = None, page: str | None = None, show_files_hidden_by_limit: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`
- **Params**: `token` — query · `user` — query · `channel` — query · `ts_from` — query · `ts_to` — query · `types` — query · `count` — query · `page` — query · `show_files_hidden_by_limit` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `FilesListschema`
- **Returns (raw)**: `ApiResult[FilesListschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `FilesListschema` | `slack_web_api/models/files_listschema.py` |

### client.files.files_remote_add

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

### client.files.files_remote_info

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

### client.files.files_remote_list

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

### client.files.files_remote_remove

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

### client.files.files_remote_share

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

### client.files.files_remote_update

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

### client.files.files_revoke_public_url

- **Route**: `POST /files.revokePublicURL`
- **Signature**: `def files_revoke_public_url(content_type: ContentTypeOrStr, *, token: str | None = None, file: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`
- **Params**: `content_type` — header `Content-Type` · `token` — header · `file` — form field
- **Returns (parsed)**: `FilesRevokePublicUrlschema`
- **Returns (raw)**: `ApiResult[FilesRevokePublicUrlschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `FilesRevokePublicUrlschema` | `slack_web_api/models/files_revoke_public_urlschema.py` |

### client.files.files_shared_public_url

- **Route**: `POST /files.sharedPublicURL`
- **Signature**: `def files_shared_public_url(content_type: ContentTypeOrStr, *, token: str | None = None, file: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`
- **Params**: `content_type` — header `Content-Type` · `token` — header · `file` — form field
- **Returns (parsed)**: `FilesSharedPublicUrlschema`
- **Returns (raw)**: `ApiResult[FilesSharedPublicUrlschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `FilesSharedPublicUrlschema` | `slack_web_api/models/files_shared_public_urlschema.py` |

### client.files.files_upload

- **Route**: `POST /files.upload`
- **Signature**: `def files_upload(content_type: ContentTypeOrStr, *, token: str | None = None, file: str | None = None, content: str | None = None, filetype: str | None = None, filename: str | None = None, title: str | None = None, initial_comment: str | None = None, channels: str | None = None, thread_ts: float | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`
- **Params**: `content_type` — header `Content-Type` · `token` — form field · `file` — form field · `content` — form field · `filetype` — form field · `filename` — form field · `title` — form field · `initial_comment` — form field · `channels` — form field · `thread_ts` — form field
- **Returns (parsed)**: `FilesUploadschema`
- **Returns (raw)**: `ApiResult[FilesUploadschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `FilesUploadschema` | `slack_web_api/models/files_uploadschema.py` |

