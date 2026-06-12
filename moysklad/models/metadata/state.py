from pydantic import BaseModel
from moysklad.models.base import Meta

class State(BaseModel):
    meta: Meta
    id: str
    accountId: str
    name: str
    color: int
    stateType: str
    entityType: str
