from pydantic import BaseModel
from moysklad.models.base import Meta

class Webhook(BaseModel):
    meta: Meta
    id: str
    accountId: str
    entityType: str
    url: str
    method: str | None = None
    enabled: bool = True
    action: str
