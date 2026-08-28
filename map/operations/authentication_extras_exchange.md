<!-- Generated file — do not edit; regenerated with the SDK. -->

# AuthenticationExtrasExchange — operations

Accessor: `client.authentication_extras_exchange` · Source: `vimeo/apis/authentication_extras_exchange.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.authentication_extras_exchange.exchange_auth_code

- **Route**: `POST /oauth/access_token`
- **Signature**: `def exchange_auth_code(body: OauthAccessTokenRequest | OauthAccessTokenRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AuthModel`
- **Returns (raw)**: `ApiResult[AuthModel, ExchangeAuthCodeErrorBody]`
- **Error**: `ExchangeAuthCodeErrorBody` — **Case A (typed)**
- **Error arms**: `AuthError` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `OauthAccessTokenRequest` | `vimeo/models/oauth_access_token_request.py` |
| `OauthAccessTokenRequestDict` | `vimeo/models/oauth_access_token_request.py` |
| `AuthModel` | `vimeo/models/auth_model.py` |
| `ExchangeAuthCodeErrorBody` | `vimeo/errors/exchange_auth_code_error.py` |
| `AuthError` | `vimeo/models/auth_error.py` |

