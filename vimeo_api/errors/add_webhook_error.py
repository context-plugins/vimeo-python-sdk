from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

AddWebhookErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _AddWebhookError:
    def map(self, response: HttpResponse) -> AddWebhookErrorBody:
        match response.status_code:
            case 400:
                return decode_json[Error](response)
            case _:
                return RawError(response)


add_webhook_error_mapper: Final[ErrorMapper[AddWebhookErrorBody]] = _AddWebhookError()
