<!-- Generated file — do not edit; regenerated with the SDK. -->

# AuthenticationExtrasEssentials — operations

Accessor: `client.authentication_extras_essentials` · Source: `vimeo/apis/authentication_extras_essentials.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.authentication_extras_essentials.delete_token

- **Route**: `DELETE /tokens`
- **Signature**: `def delete_token(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteTokenErrorBody]`
- **Error**: `DeleteTokenErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteTokenErrorBody` | `vimeo/errors/delete_token_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.authentication_extras_essentials.verify_token

- **Route**: `GET /oauth/verify`
- **Signature**: `def verify_token(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `AuthModel`
- **Returns (raw)**: `ApiResult[AuthModel, VerifyTokenErrorBody]`
- **Error**: `VerifyTokenErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AuthModel` | `vimeo/models/auth_model.py` |
| `VerifyTokenErrorBody` | `vimeo/errors/verify_token_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

