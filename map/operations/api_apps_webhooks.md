<!-- Generated file — do not edit; regenerated with the SDK. -->

# ApiAppsWebhooks — operations

Accessor: `client.api_apps_webhooks` · Source: `vimeo/apis/api_apps_webhooks.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.api_apps_webhooks.add_webhook

- **Route**: `POST /apps/{app_id}/webhooks`
- **Signature**: `def add_webhook(app_id: float, *, body: AppsWebhooksRequest | AppsWebhooksRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `app_id`
- **Params**: `app_id` — path · `body` — JSON body
- **Returns (parsed)**: `ApiAppWebhook`
- **Returns (raw)**: `ApiResult[ApiAppWebhook, AddWebhookErrorBody]`
- **Error**: `AddWebhookErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AppsWebhooksRequest` | `vimeo/models/apps_webhooks_request.py` |
| `AppsWebhooksRequestDict` | `vimeo/models/apps_webhooks_request.py` |
| `ApiAppWebhook` | `vimeo/models/api_app_webhook.py` |
| `AddWebhookErrorBody` | `vimeo/errors/add_webhook_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.api_apps_webhooks.delete_webhook

- **Route**: `DELETE /apps/{app_id}/webhooks/{webhook_id}`
- **Signature**: `def delete_webhook(app_id: float, webhook_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `app_id`, `webhook_id`
- **Params**: `app_id` — path · `webhook_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteWebhookErrorBody]`
- **Error**: `DeleteWebhookErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteWebhookErrorBody` | `vimeo/errors/delete_webhook_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.api_apps_webhooks.get_webhook

- **Route**: `GET /apps/{app_id}/webhooks/{webhook_id}`
- **Signature**: `def get_webhook(app_id: float, webhook_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `app_id`, `webhook_id`
- **Params**: `app_id` — path · `webhook_id` — path
- **Returns (parsed)**: `ApiAppWebhook`
- **Returns (raw)**: `ApiResult[ApiAppWebhook, GetWebhookErrorBody]`
- **Error**: `GetWebhookErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ApiAppWebhook` | `vimeo/models/api_app_webhook.py` |
| `GetWebhookErrorBody` | `vimeo/errors/get_webhook_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.api_apps_webhooks.get_webhooks

- **Route**: `GET /apps/{app_id}/webhooks`
- **Signature**: `def get_webhooks(app_id: float, *, page: float | None = None, per_page: float | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `app_id`
- **Params**: `app_id` — path · `page` — query · `per_page` — query
- **Returns (parsed)**: `ApiAppWebhookConnection`
- **Returns (raw)**: `ApiResult[ApiAppWebhookConnection, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApiAppWebhookConnection` | `vimeo/models/api_app_webhook_connection.py` |

### client.api_apps_webhooks.update_webhook

- **Route**: `PATCH /apps/{app_id}/webhooks/{webhook_id}`
- **Signature**: `def update_webhook(app_id: float, webhook_id: float, *, body: AppsWebhooksRequest1 | AppsWebhooksRequest1Dict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `app_id`, `webhook_id`
- **Params**: `app_id` — path · `webhook_id` — path · `body` — JSON body
- **Returns (parsed)**: `ApiAppWebhook`
- **Returns (raw)**: `ApiResult[ApiAppWebhook, UpdateWebhookErrorBody]`
- **Error**: `UpdateWebhookErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AppsWebhooksRequest1` | `vimeo/models/apps_webhooks_request1.py` |
| `AppsWebhooksRequest1Dict` | `vimeo/models/apps_webhooks_request1.py` |
| `ApiAppWebhook` | `vimeo/models/api_app_webhook.py` |
| `UpdateWebhookErrorBody` | `vimeo/errors/update_webhook_error.py` |
| `Error` | `vimeo/models/error.py` |

