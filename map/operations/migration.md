<!-- Generated file — do not edit; regenerated with the SDK. -->

# Migration — operations

Accessor: `client.migration` · Source: `slack_web_api/apis/migration.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.migration.migration_exchange

- **Route**: `GET /migration.exchange`
- **Signature**: `def migration_exchange(token: str, users: str, content_type: ContentTypeOrStr, *, team_id: str | None = None, to_old: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `users`, `content_type`
- **Params**: `token` — query · `users` — query · `team_id` — query · `to_old` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `MigrationExchangesuccessschema`
- **Returns (raw)**: `ApiResult[MigrationExchangesuccessschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `MigrationExchangesuccessschema` | `slack_web_api/models/migration_exchangesuccessschema.py` |

