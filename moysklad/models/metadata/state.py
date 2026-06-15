from pydantic import BaseModel
from moysklad.models.base import Meta

class State(BaseModel):
    meta: Meta
    id: str | None = None
    accountId: str | None = None
    name: str | None = None
    color: int | None = None
    stateType: str | None = None
    entityType: str | None = None
