<!-- Generated file — do not edit; regenerated with the SDK. -->

# EmbedPresetsFolders — operations

Accessor: `client.embed_presets_folders` · Source: `vimeo/apis/embed_presets_folders.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.embed_presets_folders.delete_folder_embed_preset

- **Route**: `DELETE /users/{user_id}/projects/{project_id}/presets/{preset_id}`
- **Signature**: `def delete_folder_embed_preset(preset_id: float, project_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `preset_id`, `project_id`, `user_id`
- **Params**: `preset_id` — path · `project_id` — path · `user_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteFolderEmbedPresetErrorBody]`
- **Error**: `DeleteFolderEmbedPresetErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteFolderEmbedPresetErrorBody` | `vimeo/errors/delete_folder_embed_preset_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

