<!-- Generated file — do not edit; regenerated with the SDK. -->

# AuthenticationExtrasConvert — operations

Accessor: `client.authentication_extras_convert` · Source: `vimeo_api/apis/authentication_extras_convert.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.authentication_extras_convert.convert_access_token

- **Route**: `POST /oauth/authorize/vimeo_oauth1`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def convert_access_token(body: OauthAuthorizeVimeoOauth1Request | OauthAuthorizeVimeoOauth1RequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AuthModel`
- **Returns (raw)**: `ApiResult[AuthModel, ConvertAccessTokenErrorBody]`
- **Error**: `ConvertAccessTokenErrorBody` — **Case A (typed)**
- **Error arms**: `AuthError` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `OauthAuthorizeVimeoOauth1Request` | `vimeo_api/models/oauth_authorize_vimeo_oauth1_request.py` |
| `OauthAuthorizeVimeoOauth1RequestDict` | `vimeo_api/models/oauth_authorize_vimeo_oauth1_request.py` |
| `AuthModel` | `vimeo_api/models/auth_model.py` |
| `ConvertAccessTokenErrorBody` | `vimeo_api/errors/convert_access_token_error.py` |
| `AuthError` | `vimeo_api/models/auth_error.py` |

