from pydantic import BaseModel
from moysklad.models.base import Meta

class Webhook(BaseModel):
    meta: Meta
    id: str | None = None
    accountId: str | None = None
    entityType: str | None = None
    url: str | None = None
    method: str | None = None
    enabled: bool = True
    action: str | None = None
