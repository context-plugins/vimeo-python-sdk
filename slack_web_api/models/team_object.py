from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.plan import PlanOrStr
from .external_org_migrations import ExternalOrgMigrations, ExternalOrgMigrationsDict
from .objs_icon import ObjsIcon, ObjsIconDict
from .objs_primary_owner import ObjsPrimaryOwner, ObjsPrimaryOwnerDict
from .sso_provider import SsoProvider, SsoProviderDict


class TeamObject(SdkBaseModel):
    archived: Optional[bool] = UNSET
    avatar_base_url: Optional[str] = UNSET
    created: Optional[int] = UNSET
    date_create: Optional[int] = UNSET
    deleted: Optional[bool] = UNSET
    description: OptionalNullable[str] = UNSET
    discoverable: Optional[Any] = UNSET
    domain: str
    email_domain: str
    enterprise_id: Optional[str] = UNSET
    enterprise_name: Optional[str] = UNSET
    external_org_migrations: Optional[ExternalOrgMigrations] = UNSET
    has_compliance_export: Optional[bool] = UNSET
    icon: ObjsIcon
    id: str
    is_assigned: Optional[bool] = UNSET
    is_enterprise: Optional[int] = UNSET
    is_over_storage_limit: Optional[bool] = UNSET
    limit_ts: Optional[int] = UNSET
    locale: Optional[str] = UNSET
    messages_count: Optional[int] = UNSET
    msg_edit_window_mins: Optional[int] = UNSET
    name: str
    over_integrations_limit: Optional[bool] = UNSET
    over_storage_limit: Optional[bool] = UNSET
    pay_prod_cur: Optional[str] = UNSET
    plan: Optional[PlanOrStr] = UNSET
    primary_owner: Optional[ObjsPrimaryOwner] = UNSET
    sso_provider: Optional[SsoProvider] = UNSET


class TeamObjectDict(TypedDict):
    archived: NotRequired[bool]
    avatar_base_url: NotRequired[str]
    created: NotRequired[int]
    date_create: NotRequired[int]
    deleted: NotRequired[bool]
    description: NotRequired[str | None]
    discoverable: NotRequired[Any]
    domain: str
    email_domain: str
    enterprise_id: NotRequired[str]
    enterprise_name: NotRequired[str]
    external_org_migrations: NotRequired[ExternalOrgMigrations | ExternalOrgMigrationsDict]
    has_compliance_export: NotRequired[bool]
    icon: ObjsIcon | ObjsIconDict
    id: str
    is_assigned: NotRequired[bool]
    is_enterprise: NotRequired[int]
    is_over_storage_limit: NotRequired[bool]
    limit_ts: NotRequired[int]
    locale: NotRequired[str]
    messages_count: NotRequired[int]
    msg_edit_window_mins: NotRequired[int]
    name: str
    over_integrations_limit: NotRequired[bool]
    over_storage_limit: NotRequired[bool]
    pay_prod_cur: NotRequired[str]
    plan: NotRequired[PlanOrStr]
    primary_owner: NotRequired[ObjsPrimaryOwner | ObjsPrimaryOwnerDict]
    sso_provider: NotRequired[SsoProvider | SsoProviderDict]
