<!-- Generated file — do not edit; regenerated with the SDK. -->

# SubscriptionPlansEssentials — operations

Accessor: `client.subscription_plans_essentials` · Source: `vimeo/apis/subscription_plans_essentials.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.subscription_plans_essentials.get_plan

- **Route**: `GET /subscription_plans/{tier}`
- **Signature**: `def get_plan(tier: Tier1OrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `tier`
- **Params**: `tier` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Tier1OrStr` | `vimeo/models/enums/tier1.py` |

