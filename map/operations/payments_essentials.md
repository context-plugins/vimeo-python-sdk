<!-- Generated file — do not edit; regenerated with the SDK. -->

# PaymentsEssentials — operations

Accessor: `client.payments_essentials` · Source: `vimeo/apis/payments_essentials.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.payments_essentials.delete_payment_method

- **Route**: `DELETE /me/payment_methods/{payment_method_id}`
- **Signature**: `def delete_payment_method(payment_method_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `payment_method_id`
- **Params**: `payment_method_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeletePaymentMethodErrorBody]`
- **Error**: `DeletePaymentMethodErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeletePaymentMethodErrorBody` | `vimeo/errors/delete_payment_method_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.payments_essentials.get_payment_method_info

- **Route**: `GET /me/payment_methods/{payment_method_id}`
- **Signature**: `def get_payment_method_info(payment_method_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `payment_method_id`
- **Params**: `payment_method_id` — path
- **Returns (parsed)**: `PaymentMethod`
- **Returns (raw)**: `ApiResult[PaymentMethod, GetPaymentMethodInfoErrorBody]`
- **Error**: `GetPaymentMethodInfoErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PaymentMethod` | `vimeo/models/payment_method.py` |
| `GetPaymentMethodInfoErrorBody` | `vimeo/errors/get_payment_method_info_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.payments_essentials.get_subscription_info

- **Route**: `GET /users/{user_id}/subscriptions/{subscription_id}`
- **Signature**: `def get_subscription_info(subscription_id: str, user_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `subscription_id`, `user_id`
- **Params**: `subscription_id` — path · `user_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.payments_essentials.list_payment_methods

- **Route**: `GET /me/payment_methods`
- **Signature**: `def list_payment_methods(*, cardmember_name: str | None = None, page: float | None = None, per_page: float | None = None, show_disabled: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `cardmember_name` — query · `page` — query · `per_page` — query · `show_disabled` — query
- **Returns (parsed)**: `PaymentMethodConnection`
- **Returns (raw)**: `ApiResult[PaymentMethodConnection, ListPaymentMethodsErrorBody]`
- **Error**: `ListPaymentMethodsErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PaymentMethodConnection` | `vimeo/models/payment_method_connection.py` |
| `ListPaymentMethodsErrorBody` | `vimeo/errors/list_payment_methods_error.py` |
| `Error` | `vimeo/models/error.py` |

