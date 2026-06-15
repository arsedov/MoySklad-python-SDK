from pydantic import BaseModel
from moysklad.models.base import Meta
from typing import Any

class AuditEvent(BaseModel):
    meta: Meta
    id: str | None = None
    accountId: str | None = None
    uid: str | None = None
    moment: str | None = None
    eventType: str | None = None
    objectType: str | None = None
    entity: dict[str, Any] | None = None
    diff: dict[str, Any] | None = None
