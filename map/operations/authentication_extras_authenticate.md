<!-- Generated file — do not edit; regenerated with the SDK. -->

# AuthenticationExtrasAuthenticate — operations

Accessor: `client.authentication_extras_authenticate` · Source: `vimeo_api/apis/authentication_extras_authenticate.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.authentication_extras_authenticate.client_auth

- **Route**: `POST /oauth/authorize/client`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def client_auth(body: OauthAuthorizeClientRequest | OauthAuthorizeClientRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AuthModel`
- **Returns (raw)**: `ApiResult[AuthModel, ClientAuthErrorBody]`
- **Error**: `ClientAuthErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `OauthAuthorizeClientRequest` | `vimeo_api/models/oauth_authorize_client_request.py` |
| `OauthAuthorizeClientRequestDict` | `vimeo_api/models/oauth_authorize_client_request.py` |
| `AuthModel` | `vimeo_api/models/auth_model.py` |
| `ClientAuthErrorBody` | `vimeo_api/errors/client_auth_error.py` |
| `Error` | `vimeo_api/models/error.py` |

