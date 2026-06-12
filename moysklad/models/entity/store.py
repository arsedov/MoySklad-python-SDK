from pydantic import BaseModel
from moysklad.models.base import Meta

class Store(BaseModel):
    meta: Meta
    id: str
    accountId: str
    updated: str
    name: str
    description: str | None = None
    code: str | None = None
    externalCode: str
    archived: bool = False
    pathName: str | None = None
