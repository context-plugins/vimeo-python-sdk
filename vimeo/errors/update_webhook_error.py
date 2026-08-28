from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

UpdateWebhookErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _UpdateWebhookError:
    def map(self, response: HttpResponse) -> UpdateWebhookErrorBody:
        match response.status_code:
            case 400:
                return decode_json[Error](response)
            case _:
                return RawError(response)


update_webhook_error_mapper: Final[ErrorMapper[UpdateWebhookErrorBody]] = _UpdateWebhookError()
