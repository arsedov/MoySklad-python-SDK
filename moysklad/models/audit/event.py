from pydantic import BaseModel
from moysklad.models.base import Meta
from typing import Any

class AuditEvent(BaseModel):
    meta: Meta
    id: str
    accountId: str
    uid: str
    moment: str
    eventType: str
    objectType: str
    entity: dict[str, Any] | None = None
    diff: dict[str, Any] | None = None
