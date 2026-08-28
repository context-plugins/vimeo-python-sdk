<!-- Generated file — do not edit; regenerated with the SDK. -->

# FilesComments — operations

Accessor: `client.files_comments` · Source: `slack_web_api/apis/files_comments.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.files_comments.files_comments_delete

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

