from typing import Any
from moysklad.models.base import BaseDocument, Meta
from pydantic import BaseModel

class DocumentPosition(BaseModel):
    meta: Meta
    id: str | None = None
    accountId: str | None = None
    quantity: float | None = None
    price: float | None = None
    discount: float | None = None
    vat: int | None = None
    assortment: dict[str, Any] | None = None

class CustomerOrder(BaseDocument):
    agent: dict[str, Any] | None = None
    positions: dict[str, Any] | None = None
