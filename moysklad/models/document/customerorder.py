from pydantic import BaseModel
from typing import Any
from moysklad.models.base import Meta

class DocumentPosition(BaseModel):
    meta: Meta
    id: str
    accountId: str
    quantity: float
    price: float
    discount: float | None = None
    vat: int | None = None
    assortment: dict[str, Any]
    
class CustomerOrder(BaseModel):
    meta: Meta
    id: str
    accountId: str
    name: str
    description: str | None = None
    updated: str
    moment: str
    applicable: bool
    sum: float
    agent: dict[str, Any]
    organization: dict[str, Any]
    state: dict[str, Any] | None = None
    positions: dict[str, Any] | None = None
