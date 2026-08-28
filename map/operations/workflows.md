<!-- Generated file — do not edit; regenerated with the SDK. -->

# Workflows — operations

Accessor: `client.workflows` · Source: `slack_web_api/apis/workflows.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.workflows.workflows_step_completed

- **Route**: `GET /workflows.stepCompleted`
- **Signature**: `def workflows_step_completed(workflow_step_execute_id: str, token: str, content_type: ContentTypeOrStr, *, outputs: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `workflow_step_execute_id`, `token`, `content_type`
- **Params**: `workflow_step_execute_id` — query · `outputs` — query · `token` — header · `content_type` — header `Content-Type`
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.workflows.workflows_step_failed

- **Route**: `GET /workflows.stepFailed`
- **Signature**: `def workflows_step_failed(workflow_step_execute_id: str, error: str, token: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `workflow_step_execute_id`, `error`, `token`, `content_type`
- **Params**: `workflow_step_execute_id` — query · `error` — query · `token` — header · `content_type` — header `Content-Type`
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.workflows.workflows_update_step

- **Route**: `GET /workflows.updateStep`
- **Signature**: `def workflows_update_step(workflow_step_edit_id: str, token: str, content_type: ContentTypeOrStr, *, inputs: str | None = None, outputs: str | None = None, step_name: str | None = None, step_image_url: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `workflow_step_edit_id`, `token`, `content_type`
- **Params**: `workflow_step_edit_id` — query · `inputs` — query · `outputs` — query · `step_name` — query · `step_image_url` — query · `token` — header · `content_type` — header `Content-Type`
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

