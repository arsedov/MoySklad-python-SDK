from pydantic import BaseModel, Field
from typing import Optional
from moysklad.models.base import Meta

class Product(BaseModel):
    meta: Meta
    id: str
    accountId: str
    owner: dict | None = None
    shared: bool = False
    group: dict | None = None
    updated: str
    name: str
    description: str | None = None
    code: str | None = None
    externalCode: str
    archived: bool = False
    pathName: str | None = None
    article: str | None = None
    weight: float | None = None
    volume: float | None = None
