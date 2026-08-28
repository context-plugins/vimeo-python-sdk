<!-- Generated file — do not edit; regenerated with the SDK. -->

# TeamProfile — operations

Accessor: `client.team_profile` · Source: `slack_web_api/apis/team_profile.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.team_profile.team_profile_get

- **Route**: `GET /team.profile.get`
- **Signature**: `def team_profile_get(token: str, content_type: ContentTypeOrStr, *, visibility: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`
- **Params**: `token` — query · `visibility` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `TeamProfileGetsuccessschema`
- **Returns (raw)**: `ApiResult[TeamProfileGetsuccessschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `TeamProfileGetsuccessschema` | `slack_web_api/models/team_profile_getsuccessschema.py` |

