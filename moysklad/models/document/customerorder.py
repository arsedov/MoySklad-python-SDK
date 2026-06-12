from typing import Any
from moysklad.models.base import BaseDocument, Meta
from pydantic import BaseModel

class DocumentPosition(BaseModel):
    meta: Meta
    id: str
    accountId: str
    quantity: float
    price: float
    discount: float | None = None
    vat: int | None = None
    assortment: dict[str, Any]

class CustomerOrder(BaseDocument):
    agent: dict[str, Any]
    positions: dict[str, Any] | None = None
