<!-- Generated file — do not edit; regenerated with the SDK. -->

# Oauth — operations

Accessor: `client.oauth` · Source: `slack_web_api/apis/oauth.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.oauth.oauth_access

- **Route**: `GET /oauth.access`
- **Signature**: `def oauth_access(content_type: ContentTypeOrStr, *, client_id: str | None = None, client_secret: str | None = None, code: str | None = None, redirect_uri: str | None = None, single_channel: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`
- **Params**: `client_id` — query · `client_secret` — query · `code` — query · `redirect_uri` — query · `single_channel` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.oauth.oauth_token

- **Route**: `GET /oauth.token`
- **Signature**: `def oauth_token(content_type: ContentTypeOrStr, *, client_id: str | None = None, client_secret: str | None = None, code: str | None = None, redirect_uri: str | None = None, single_channel: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`
- **Params**: `client_id` — query · `client_secret` — query · `code` — query · `redirect_uri` — query · `single_channel` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.oauth.oauth_v2_access

- **Route**: `GET /oauth.v2.access`
- **Signature**: `def oauth_v2_access(code: str, content_type: ContentTypeOrStr, *, client_id: str | None = None, client_secret: str | None = None, redirect_uri: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `code`, `content_type`
- **Params**: `code` — query · `client_id` — query · `client_secret` — query · `redirect_uri` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

